from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import pytest
from etude_ia.analysis import calculer_moyennes, scatterplot, boxplot

@pytest.fixture
def test_data():
    x = np.random.randint(0, 5, (100, 5))
    y = np.random.randint(0, 100, (100,)) > 50
    return x, y

def test_calculer_moyennes(test_data):
    x, y = test_data

    for c in range(5):
        moyennes = calculer_moyennes(x, y, c)

        assert isinstance(moyennes, tuple)
        assert len(moyennes) == 2
        assert ((moyennes[0] == x[y!=0, c].mean() and 
                moyennes[1] == x[y==0, c].mean()) or 
                (moyennes[1] == x[y!=0, c].mean() and 
                moyennes[0] == x[y==0, c].mean()))
        