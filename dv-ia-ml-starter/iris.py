"""Apprentissage de numpy, scikit-learn et matplotlib à 
l'aide de la base de données d'exemple "iris".
"""

from typing import Callable
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import accuracy_score


def montrer_infos(dataset: dict) -> None:
    """Affiche les informations du dataset 'iris'.
    
    :param dataset: dictionnaire récupéré par la méthode load_iris

    Ce dictionnaire contient:
    * DESCR: description complète du dataset et références.
    * data: tableau numpy avec les données des variables pour chaque individu (= plante)
    * target: tableau numpy avec les classes associées à chaque individu
    * feature_names: nom des caractéristiques (colonnes du tableau)
    * target_names: nom des classes
    """
    print(f"=== Informations sur le dataset ===")
    print(dataset['DESCR'])

    print(f"=== Récupération des données ===")
    print(f"Taille du tableau de données: {dataset['data'].shape}")
    print(f"Nom des colonnes (=caractéristiques): {dataset['feature_names']}")
    print(f"Nom des classes (=catégories): {dataset['target_names']}")
    print(f"Première ligne: {dataset['data'][0]}")
    print(f"Première classe: {dataset['target'][0]} = {dataset['target_names'][dataset['target'][0]]}")


def afficher_scatterplots(X: np.ndarray, Y: np.ndarray) -> None:
    """Afficher les scatterplots suivants:
    
    sepal length vs sepal width
    petal length vs petal width
    sepal length vs petal length
    sepal width vs petal width

    Avec à chaque fois une couleur différente par classe
    """

    ## -- code à faire ensemble -- #
    ## - séparer le tableau X en fonction de la classe Y
    ## - récupérer les colonnes désirées
    ## - afficher un scatterplot avec matplotlib

    return


def calcul_moyennes(X: np.ndarray, Y: np.ndarray) -> dict[int, list[float]]:
    """Calculer pour chaque classe la valeur moyenne de chaque variable.
    
    Renvoie un dictionnaire avec comme clé le numéro de la classe (0, 1, 2) et comme 
    valeur une liste de float (un float par variable) contenant les moyennes.
    
    :param X: tableau de données
    :param Y: tableau (à une dimansion) des classes
    """
    result: dict[int, list[float]] = {}

    # -- votre code ici -- #

    return result


def classifier_plante(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float) -> int:
    """Classification manuelle: créer une fonction permettant de déterminer la catégorie (0, 1, 2) 
    selon les valeurs des 4 caractéristiques.

    À créer en fonction de ce que vous observez dans les scatterplot et les moyennes.
    
    :param sepal_length:
    :param sepal_width:
    :param petal_length:
    :param petal_width:

    :return: entier représentant la catégorie (0, 1, 2)
    """

    return np.random.randint(0, 3)


def evaluer_classificateur(X: np.ndarray, Y: np.ndarray, fn_classif: Callable[[float, float, float, float], int]) -> float:
    """Évalue une fonction de classification sur le dataset.
    
    Renvoie la valeur d'exactitude (accuracy), soit le nombre de cas bien classifié divisé par le nombre de 
    cas total."""
    predictions = []
    for sl, sw, pl, pw in X:
        predictions.append(fn_classif(sl, sw, pl, pw))
    
    correct = [p==t for p, t in zip(predictions, Y)]
    return sum(correct)/len(correct)


def classif_scikit_learn(X: np.ndarray, Y: np.ndarray) -> None:
    """Utilise un classificateur de scikit-learn sur le dataset, avec une phase 
    d'entraînement, une phase d'évaluation, et une séparation du dataset en set 
    d'entraînement et set de test.
    """

    ## -- code à faire ensemble -- #
    # - séparer les données en ensemble de test et d'entraînement
    # - instanciation d'un RidgeClassifier
    # - entraînement
    # - prédiction
    # - évaluation avec accuracy_score
    
    return


def main() -> None:
    dataset = load_iris()
    montrer_infos(dataset)

    X = dataset['data']
    Y = dataset['target']

    afficher_scatterplots(X, Y)

    moyennes = calcul_moyennes(X, Y)
    print(moyennes)

    acc = evaluer_classificateur(X, Y, classifier_plante)
    print(f"Exactitude: {100*acc:.2f}%")

    classif_scikit_learn(X, Y)


if __name__ == "__main__":
    main()
