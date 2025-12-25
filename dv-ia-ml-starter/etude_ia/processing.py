"""Méthodes relatives au pré-traitement des données.
"""
import itertools

import numpy as np
from sklearn.model_selection import train_test_split


def filtrer_donnees_manquantes(donnees: list[list[str]]) -> list[list[str]]:
    """Renvoie une liste dans laquelle toute ligne contenant au moins un 
    'nan' a été retirée
    
    :param donnees: liste avec tous les individus de l'étude.
    :return: liste avec les individus pour lesquels toutes les données sont présentes.
    """
    donnees_filtrees = []

    ## -- votre code ici -- ##
    for line in donnees:
        lineOk = True
        for data in line:
            if(data == 'nan'):
                lineOk = False
                break
        if(lineOk):
            donnees_filtrees.append(line)

    # ou autre solution:

    # return [line for line in donnes if 'nan' not in line]
                

    return donnees_filtrees


def convertir_donnees(donnees: list[list[str]]) -> np.ndarray:
    """Renvoie un tableau numpy contenant toutes les données sous forme d'entier.
    
    :param donnees: liste avec toutes les données sous forme de listes de `str`
    :return: les mêmes données converties en `int` sous forme de numpy array
    """

    ## -- votre code ici -- ##
    ## n'oubliez pas d'ajouter la valeur de return! ##
    

    return 


def preparer_dataset(donnees: np.ndarray) -> tuple[np.ndarray, 
                                                   np.ndarray,
                                                   np.ndarray,
                                                   np.ndarray]:
    """Sépare les données en quatre tableaux numpy:
    
    Xtrain: variables du set d'entraînement sans le "target"
    Xtest: variables du set de test
    Ytrain: target du set d'entraînement = réussite ou non (réussite = note > 50)
    Ytest: target du set de test
    
    Le set de test doit contenir 25% des données.

    :param donnees: array numpy contenant des valeurs entières
    :return: tuple Xtrain, Xtest, Ytrain, Ytest

    Ytest et Ytrain doivent contenir des valeurs booléennes
    """

    ## -- votre code ici -- ##
    ## n'oubliez pas d'ajouter la valeur de return! ##

    return 