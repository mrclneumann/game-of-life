import os

import numpy as np
from scipy.signal import convolve
import time


def update(grid):
    neighbors = convolve(in1=grid, in2=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], mode="same")

    return ((grid == 0) & (neighbors == 3)) | (
        (grid == 1) & (np.isin(neighbors, [2, 3]))
    )


def print_grid(grid):
    print("\n".join(["".join(["x" if cell else " " for cell in row]) for row in grid]))


if __name__ == "__main__":
    grid = np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )

    print_grid(grid)
    while True:
        time.sleep(1)
        os.system("clear")
        grid = update(grid)
        print_grid(grid)
