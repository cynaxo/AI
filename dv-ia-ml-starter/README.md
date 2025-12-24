# Starter pack - exercice Machine Learning

Code de démarrage pour l'exercice complet "Machine Learning avec Python".

Les **fichiers à modifier** sont ceux dans le dossier `etude_ia`.

1. `data.py` pour l'acquisition des données
2. `processing.py` pour le pré-traitement
3. `analysis.py` pour l'analyse et la visualisation
4. `classifier.py` pour l'entraînement et l'évaluation

## Utilisation

*Instructions plus détaillées avec PyCharm disponibles ici: [https://vinci.adfoucart.be/ia/seance_5_instructions.html](https://vinci.adfoucart.be/ia/seance_5_instructions.html)*

1. Créer un environnement virtuel et installez-y les librairies dans `requirements.txt`, soit via l'interface de PyCharm, soit via la ligne de commande:

Unix:

```
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Windows:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Exécuter le programme: `python main.py` (avec l'environnement virtuel actif)

3. Exécuter les tests: `pytest` (depuis le répertoire où se trouve `main.py`, et avec l'environnement virtuel actif)

## Sortie attendue du programme (début de l'exercice)

`python main.py` devrait donner:

```
Démarrage du programme.
 -- Acquisition --
Trouvé 0 instituts
0 participant.e.s à l'étude
Colonnes: []
 -- Pré-traitement --
0 participant.e.s sans données manquantes.
Traceback (most recent call last):
  File "/home/adrien/workspace/dv-ia-ml-starter/main.py", line 67, in <module>
    main()
  File "/home/adrien/workspace/dv-ia-ml-starter/main.py", line 33, in main
    print(f"Les données sont maintenant un tableau de taille {donnees.shape} et de type {donnees.dtype}")
                                                              ^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'shape'
```

`pytest` devrait donner:

```
... (beaucoup de lignes avec beaucoup de rouge)
=================== short test summary info ======================
FAILED tests/test_analysis.py::test_calculer_moyennes - assert False
FAILED tests/test_classifier.py::test_entrainer_arbre_decision - assert False
FAILED tests/test_classifier.py::test_evaluer_arbre_decision - assert 0.0 == 0.66
FAILED tests/test_data.py::test_charger_instituts - AssertionError: assert [] == [{'fichier': ...ipants': 122}]
FAILED tests/test_data.py::test_charger_donnees - assert 0 == 859
FAILED tests/test_data.py::test_charger_noms_colonnes - AssertionError: assert [] == ['id_student'..., 'note_exam']
FAILED tests/test_processing.py::test_filtrer_donnees_manquantes - assert 0 == 7
FAILED tests/test_processing.py::test_convertir_donnees - AssertionError: assert False
FAILED tests/test_processing.py::test_preparer_dataset - assert False
=================== 9 failed in 1.45s ============================
```

## Sortie attendue du programme (fin de l'exercice)

`python main.py` devrait donner quelque chose de très similaire (les chiffres peuvent varier pour les scores à la fin) à:

```
Démarrage du programme.
 -- Acquisition --
Trouvé 5 instituts
673 participant.e.s à l'étude
Colonnes: ['id_student', 'freq_util', 'verif_sources', 'model_quality', 'prompt_quality', 'note_exam']
 -- Pré-traitement --
610 participant.e.s sans données manquantes.
Les données sont maintenant un tableau de taille (610, 6) et de type int64
Set d'entraînement: 457 étudiant.e.s, dont 172 ont réussi
Set de test: 153 étudiant.e.s, dont 52 ont réussi
 -- Analyse --
Moyenne pour id_student: 148.78 (Réussi), 130.88 (Raté)
Moyenne pour freq_util: 2.52 (Réussi), 2.76 (Raté)
Moyenne pour verif_sources: 2.60 (Réussi), 1.39 (Raté)
Moyenne pour model_quality: 2.92 (Réussi), 1.88 (Raté)
Moyenne pour prompt_quality: 2.70 (Réussi), 1.60 (Raté)
scatter_1_4.png sauvegardé
boxplot_3.png sauvegardé
 -- Entraînement --
Classificateur entraîné.
arbre.png sauvegardé
 -- Évaluation -- 
Exactitude sur les données d'entraînement: 76.84%
Exactitude sur les données de test: 68.37%
```

Vous devriez également avoir les images `arbre.png`, `boxplot_3.png` et `scatter_1_4.png` dans le même dossier que `main.py`.

`pytest` devrait donner:

```
============================= test session starts ===========================
...
collected 9 items

tests/test_analysis.py ...      [ 27%]
tests/test_classifier.py ..     [ 45%]
tests/test_data.py ...          [ 72%]
tests/test_processing.py ...    [100%]

============================= 9 passed in 0.66s ===========================

```