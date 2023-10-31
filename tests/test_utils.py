import numpy as np

from nlp_engineer_assignment.utils import count_letters, score


def test_count_letters():
    assert np.array_equal(count_letters("hello"), np.array([0, 0, 0, 1, 0]))
    assert np.array_equal(count_letters("world"), np.array([0, 0, 0, 0, 0]))
    assert np.array_equal(
        count_letters("hello hello"),
        np.array([0, 0, 0, 1, 0, 0, 1, 1, 2, 2, 1])
    )


def test_score():
    assert score(np.array([[0, 1, 1, 0, 1]]),
                 np.array([[0, 1, 1, 0, 1]])) == 1.0
    assert score(np.array([[0, 1, 1, 0, 1]]),
                 np.array([[1, 1, 0, 0, 1]])) == 0.6
    assert score(np.array([[0, 1, 1, 0, 1]]),
                 np.array([[0, 0, 0, 0, 0]])) == 0.4
    assert score(np.array([[0, 1, 1, 0, 1]]),
                 np.array([[1, 0, 0, 1, 0]])) == 0.0
