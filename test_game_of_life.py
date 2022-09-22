import numpy as np
import pytest
from numpy.testing import assert_array_equal

from game_of_life import update


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[1, 0, 0], [0, 1, 1], [0, 0, 0]], [[0, 1, 0], [0, 1, 0], [0, 0, 0]]),
    ],
)
def test_update(grid, expected):
    assert_array_equal(update(np.array(grid)), expected)


def test_blinker():
    assert_array_equal(
        update(np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])),
        [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
    )


@pytest.mark.parametrize(
    "grid",
    [
        [[1, 1], [1, 1]],
        [[0, 1, 0], [1, 0, 1], [0, 1, 0]],
        [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]],
    ],
    ids=["block", "tub", "pond"],
)
def test_static_objects(grid):
    assert_array_equal(update(np.array(grid)), grid)
