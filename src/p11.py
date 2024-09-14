import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = np.zeros(len(b), dtype=float)
    for _ in range(n):
        y = x.copy()
        for i in range(len(x)):
            y[i] = (1/A[i][i]) * (
                b[i] - sum(A[i][j] * x[j] for j in range(len(x)))
                + A[i][i] * x[i]
                )
            y[i] = round(y[i], 4)
        x = y.copy()
    return x.tolist()
