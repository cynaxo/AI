import csv
import json
import pathlib
import pytest

from etude_ia.data import charger_donnees_etude, charger_instituts

@pytest.fixture
def instituts_test():
    return [
        {
            "institut": "Test 1",
            "fichier": "test_1.csv",
            "participants": 506
        },
        {
            "institut": "Test 2",
            "fichier": "test_2.csv",
            "participants": 231
        },
        {
            "institut": "Test 3",
            "fichier": "test_3.csv",
            "participants": 122
        }
    ]

@pytest.fixture
def noms_colonnes():
    return ["id_student","freq_util","verif_sources","model_quality","prompt_quality","note_exam"]


def fake_instituts(repertoire: pathlib.Path, instituts: list[dict]):
    with open(repertoire.joinpath("dataset.json"), "w") as fp:
        json.dump(instituts, fp)


def fake_data(repertoire: pathlib.Path, 
              instituts: list[dict],
              colonnes: list[str]) -> list[str]:
    fichiers = []
    for institut in instituts:
        fichier = repertoire.joinpath(institut["fichier"])
        fichiers.append(str(fichier))
        with open(fichier, "w", newline="") as fp:
            writer = csv.writer(fp)
            writer.writerow(colonnes)
            writer.writerows([["0" for _ in range(6)] for _ in range(institut["participants"])])
    return fichiers


def test_charger_instituts(tmp_path, instituts_test):
    fake_instituts(tmp_path, instituts_test)
    instituts = charger_instituts(tmp_path)

    assert isinstance(instituts, list)
    assert instituts == instituts_test


def test_charger_donnees(tmp_path, instituts_test, noms_colonnes):
    fichiers = fake_data(tmp_path, instituts_test, noms_colonnes)
    _, donnees = charger_donnees_etude(fichiers)

    assert isinstance(donnees, list)
    assert len(donnees) == sum(institut["participants"] for institut in instituts_test)
    assert all(len(ligne) == 6 for ligne in donnees)
    assert all(all(isinstance(element, str) for element in ligne) for ligne in donnees)


def test_charger_noms_colonnes(tmp_path, instituts_test, noms_colonnes):
    fichiers = fake_data(tmp_path, instituts_test, noms_colonnes)
    
    noms_colonnes, _ = charger_donnees_etude(fichiers)

    assert noms_colonnes == ["id_student","freq_util","verif_sources","model_quality","prompt_quality","note_exam"]
    