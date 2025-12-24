"""Méthodes relatives au chargement des données.
"""
import json
import csv
import os

def charger_instituts(repertoire: str) -> list[dict]:
    """Récupérer le contenu du fichier dataset.json
    sous forme d'une liste de dictionnaires.

    :param repertoire: chemin vers le dossier où se trouve le fichier dataset.json
    :return: liste des dictionnaires avec les informations sur les instituts
    """
    fichier = os.path.join(repertoire, "dataset.json")

    instituts: list[dict] = []

    with open(fichier, "r") as fp:
        instituts: list[dict] = json.load(fp)

    return instituts


def charger_donnees_institut(fichier: str) -> tuple[list[str], list[list[str]]]:
    """Charger les données contenues dans un fichier .csv.

    Renvoie les noms de colonnes sous forme de liste de str, et les 
    données sous forme d'une liste de listes de `str`.

    :param fichier: chemin vers le fichier .csv
    :return: tuple (noms de colonnes, données)
    """
    data: list[list[str]] = []
    with open(fichier, "r") as fp:
        reader = csv.reader(fp)
        data = [row for row in reader]

    return data[0], data[1:]


def charger_donnees_etude(fichiers: list[str]) -> tuple[list[str], list[list[str]]]:
    """Charger l'ensemble des données contenues dans les fichiers .csv 
    de l'étude et les coller ensemble dans une liste de listes.

    Renvoie les noms de colonnes sous forme de liste de str, et les 
    données sous forme d'une liste de listes de `str`.

    :param fichiers: chemin (relatif ou absolu) vers les fichiers .csv à charger
    :return: tuple (noms de colonnes, données)
    """
    donnees: list[list[str]] = []
    noms_colonnes: list[str] = []

    for fichier in fichiers:
        noms_colonnes, donnes_du_fichier = charger_donnees_institut(fichier)
        donnees.extend(donnes_du_fichier)         
        
        ## -- votre code ici -- ##

    return noms_colonnes, donnees
