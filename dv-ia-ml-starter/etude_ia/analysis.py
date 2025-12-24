"""Méthodes relatives à l'analyse des données:

- Affichage de graphiques
- Calcul de statistiques descriptives
"""


from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import numpy as np


def calculer_moyennes(x: np.ndarray, y: np.ndarray, colonne: int) -> tuple[float, float]:
    """Renvoie la moyenne de la colonne choisie pour les étudiant.e.s ayant raté et réussi.

    :param x: données de l'étude (sans le target)
    :param y: booléens marquant si l'étudiant.e à réussi (True) ou non
    :return: tuple avec la valeur moyenne de la colonne choisie pour les étudiant.e.s ayant réussi, 
        et pour les étudiant.e.s qui ont raté.
    """

    ## -- votre code ici -- ##

    return 


def scatterplot(x: np.ndarray, y: np.ndarray, colonne_x: int, colonne_y: int) -> Figure:
    """Génère une figure matplotlib avec un scatterplot dans lequel 
    les points sont coloré selon le target y, et les axes x et y sont 
    définis par les colonnes choisies.
    
    :param x: données de l'étude (sans le target)
    :param y: booléens marquant si l'étudiant.e à réussi (True) ou non
    :return: la figure"""

    fig, ax = plt.subplots()

    ax.scatter(x[y==True, colonne_x], x[y==True, colonne_y], marker='o', color='b', alpha=0.5, label='Réussi')
    ax.scatter(x[y==False, colonne_x], x[y==False, colonne_y], marker='o', color='r', alpha=0.5, label='Raté')
    ax.legend()

    return fig


def boxplot(x: np.ndarray, y: np.ndarray, colonne: int) -> Figure:
    """Génère une figure matplotlib avec un boxplot avec les distributions 
     des étudiant.e.s ayant raté et réussi pour la colonne donnée.
    
    :param x: données de l'étude (sans le target)
    :param y: booléens marquant si l'étudiant.e à réussi (True) ou non
    :return: la figure"""
    fig, ax = plt.subplots()

    ax.boxplot([x[y==True, colonne], x[y==False, colonne]], tick_labels=["Réussi", "Raté"])

    return fig
