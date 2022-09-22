import numpy as np
from numpy._typing import ArrayLike
from scipy.signal import convolve


def update(grid: ArrayLike):
    window = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    neighbors = convolve(in1=grid, in2=window, mode="same")

    return ((grid == 0) & (neighbors == 3)) | (
        (grid == 1) & (np.isin(neighbors, [2, 3]))
    )
