import numpy as np


def feature_scaling(data: np.ndarray) -> np.ndarray:
    column_mean = data.mean(axis=0)
    column_std = data.std(axis=0)
    standardized_data = (data - column_mean) / column_std
    return standardized_data


def pca(data: np.ndarray, k: int) -> list[list[int | float]]:
    cov_matrix = np.cov(feature_scaling(data=data), rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    sort_index = np.flip(np.argsort(eigenvalues))
    sorted_eigenvectors = eigenvectors[:, sort_index]
    principal_components = sorted_eigenvectors[:, :k]
    return np.round(principal_components, decimals=4)
