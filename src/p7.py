import numpy as np


def transform_matrix(
        A: list[list[int | float]],
        T: list[list[int | float]],
        S: list[list[int | float]]
        ) -> list[list[int | float]]:
    matrix_a = np.array(A)
    matrix_t = np.array(T)
    matrix_s = np.array(S)
    if not np.linalg.det(matrix_t):
        return -1
    if not np.linalg.det(matrix_s):
        return -1
    return np.dot(np.linalg.inv(matrix_t), np.dot(matrix_a, matrix_s))
