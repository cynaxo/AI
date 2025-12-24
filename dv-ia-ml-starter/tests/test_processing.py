import numpy as np
from etude_ia.processing import convertir_donnees, filtrer_donnees_manquantes, preparer_dataset
import pytest

@pytest.fixture
def test_data() -> list[list[str]]:
    return [
        ["a", "b", "c", "d", "e", "f"],
        ["a", "b", "c", "d", "e", "f"],
        ["a", "b", "nan", "d", "e", "f"],
        ["a", "b", "c", "d", "e", "f"],
        ["a", "b", "c", "d", "e", "f"],
        ["a", "b", "c", "nan", "e", "f"],
        ["a", "b", "c", "d", "e", "f"],
        ["a", "b", "c", "d", "e", "f"],
        ["nan", "nan", "nan", "d", "e", "f"],
        ["a", "b", "c", "d", "e", "f"]
    ]

@pytest.fixture
def test_data_filtered() -> list[list[str]]:
    return [
        [str(i*10+j) for j in range(6)] for i in range(100)
    ]

def test_filtrer_donnees_manquantes(test_data):
    donnees_filtrees = filtrer_donnees_manquantes(test_data)

    assert len(donnees_filtrees) == 7
    assert all(len(ligne)==6 for ligne in donnees_filtrees)


def test_convertir_donnees(test_data_filtered):
    donnees = convertir_donnees(test_data_filtered)

    assert isinstance(donnees, np.ndarray)
    assert donnees.shape == (100, 6)
    assert issubclass(donnees.dtype.type, np.integer)


def test_preparer_dataset(test_data_filtered):
    donnees = np.array(test_data_filtered, dtype='int')

    ds = preparer_dataset(donnees)

    assert isinstance(ds, tuple)
    assert len(ds) == 4
    assert all(isinstance(x, np.ndarray) for x in ds)

    Xtrain, Xtest, Ytrain, Ytest = ds
    assert len(Xtrain) == len(Ytrain)
    assert len(Xtest) == len(Ytest)
    assert len(Xtest) == len(donnees)//4
    assert len(Xtrain) == len(donnees)-len(Xtest)
    assert issubclass(Xtrain.dtype.type, np.integer)
    assert issubclass(Xtest.dtype.type, np.integer)
    assert issubclass(Ytrain.dtype.type, np.bool)
    assert issubclass(Ytest.dtype.type, np.bool)

    total_positives = sum(donnees[:, -1] > 50)
    assert sum(Ytrain)+sum(Ytest) == total_positives