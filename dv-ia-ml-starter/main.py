import os
import random

from matplotlib import pyplot as plt
import numpy as np

from etude_ia.data import charger_instituts, charger_donnees_etude
from etude_ia.processing import convertir_donnees, filtrer_donnees_manquantes, preparer_dataset
from etude_ia.analysis import calculer_moyennes, scatterplot, boxplot
from etude_ia.classifier import afficher_arbre, entrainer_arbre_decision, evaluer_arbre_decision

DATADIR = "./data" # à adapter si nécessaire

def main():
    # fixer les random seed pour que le programme soit déterministe
    random.seed(0)
    np.random.seed(0)

    print("Démarrage du programme.")
    
    print(" -- Acquisition --")
    instituts = charger_instituts(DATADIR)
    print(f"Trouvé {len(instituts)} instituts")
    fichiers = [os.path.join(DATADIR, institut["fichier"]) for institut in instituts]
    noms_colonnes, donnees = charger_donnees_etude(fichiers)
    print(f"{len(donnees)} participant.e.s à l'étude")
    print(f"Colonnes: {noms_colonnes}")
    
    print(" -- Pré-traitement --")
    donnees = filtrer_donnees_manquantes(donnees)
    print(f"{len(donnees)} participant.e.s sans données manquantes.")
    donnees = convertir_donnees(donnees)
    print(f"Les données sont maintenant un tableau de taille {donnees.shape} et de type {donnees.dtype}")
    Xtrain, Xtest, Ytrain, Ytest = preparer_dataset(donnees)
    print(f"Set d'entraînement: {Xtrain.shape[0]} étudiant.e.s, dont {Ytrain.sum()} ont réussi")
    print(f"Set de test: {Xtest.shape[0]} étudiant.e.s, dont {Ytest.sum()} ont réussi")

    print(" -- Analyse --")
    for colonne in range(5):
        moy_reussi, moy_rate = calculer_moyennes(Xtrain, Ytrain, colonne)
        print(f"Moyenne pour {noms_colonnes[colonne]}: {moy_reussi:.2f} (Réussi), {moy_rate:.2f} (Raté)")
    fig_a = scatterplot(Xtrain, Ytrain, colonne_x=1, colonne_y=4)
    fig_a.savefig("scatter_1_4.png")
    print("scatter_1_4.png sauvegardé")
    plt.close(fig_a)
    fig_b = boxplot(Xtrain, Ytrain, colonne=3)
    fig_b.savefig("boxplot_3.png")
    print("boxplot_3.png sauvegardé")
    plt.close(fig_b)

    print(" -- Entraînement --")
    clf = entrainer_arbre_decision(Xtrain, Ytrain)
    print("Classificateur entraîné.")
    fig_tree = afficher_arbre(clf, noms_colonnes, ["Raté", "Réussi"])
    fig_tree.savefig("arbre.png")
    print("arbre.png sauvegardé")

    print(" -- Évaluation -- ")
    score_train, score_test = evaluer_arbre_decision(clf, Xtrain, Ytrain, Xtest, Ytest)
    print(f"Exactitude sur les données d'entraînement: {score_train*100:.2f}%")
    print(f"Exactitude sur les données de test: {score_test*100:.2f}%")

    print("Fin du programme.")


if __name__ == "__main__":
    main()
