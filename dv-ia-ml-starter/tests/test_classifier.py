import numpy as np
import pytest
from etude_ia.classifier import entrainer_arbre_decision, evaluer_arbre_decision
from sklearn.tree import DecisionTreeClassifier


@pytest.fixture
def test_data():
    x = np.random.randint(0, 5, (100, 5))
    y = np.random.randint(0, 100, (100,)) > 50
    return x, y


def test_entrainer_arbre_decision(test_data):
    x, y = test_data
    clf = entrainer_arbre_decision(x, y)

    assert isinstance(clf, DecisionTreeClassifier)
    assert len(clf.classes_) == 2


def test_evaluer_arbre_decision(test_data):
    x, y = test_data
    clf = DecisionTreeClassifier(max_depth=2)
    clf.fit(x[:50], y[:50])

    scores = evaluer_arbre_decision(clf, 
                                    x[:50], 
                                    y[:50], 
                                    x[50:],
                                    y[50:])
    
    assert isinstance(scores, tuple)
    assert len(scores) == 2

    score_train, score_test = scores
    assert score_train == clf.score(x[:50], y[:50])
    assert score_test == clf.score(x[50:], y[50:])
    