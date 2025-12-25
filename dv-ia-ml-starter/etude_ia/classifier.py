"""Méthodes relatives à l'entraînement et l'évaluation d'un classificateur.
"""

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree


def entrainer_arbre_decision(x: np.ndarray, y: np.ndarray) -> DecisionTreeClassifier:
    """Crée un DecisionTreeClassifier. Entraîne le classificateur avec les 
    données x, y, et renvoie le classificateur entraîné.
    
    :param x: données d'entraînement (sans target)
    :param y: target binaire
    :return: modèle entraîné.
    """
    
    ## -- votre code ici -- ##
    ## n'oubliez pas d'ajouter la valeur de return! ##
    clf = DecisionTreeClassifier(max_depth=4)
    clf.fit(x,y)
    
    return clf


def evaluer_arbre_decision(clf: DecisionTreeClassifier, 
                           x_train: np.ndarray, 
                           y_train: np.ndarray,
                           x_test: np.ndarray,
                           y_test: np.ndarray) -> tuple[float, float]:
    """Calcule l'exactitude de la prédiction effectuée par le classificateur sur les 
    sets d'entraînement et de test.
    """
    score_train = 0.
    score_test = 0.

    # train data
    pred_train = clf.predict(x_train)
    correct_train = pred_train==y_train
    score_train = sum(correct_train)/len(correct_train)


    # test data
    pred_tes = clf.predict(x_test)
    correct_test = pred_tes==y_test
    score_test = sum(correct_test)/len(correct_test)


    return score_train, score_test


def afficher_arbre(clf: DecisionTreeClassifier, 
                   noms_colonnes: list[str],
                   noms_classes: list[str]) -> Figure:
    """Génère l'image pour l'arbre de décision.
    
    Cette fonction est complète, pas besoin de la modifier!

    :param clf: classificateur - arbre de décision
    :param nom_colonnes: liste des noms de colonnes associé aux données fournies au decision tree
    :param nom_classes: nom de catégories classifiées par le decision tree
    :return: figure matplotlib
    """
    fig, ax = plt.subplots(dpi=300)
    plot_tree(clf, feature_names=noms_colonnes, class_names=noms_classes, ax=ax, max_depth=3, filled=True)
    return fig


