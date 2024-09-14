import numpy as np


def feature_scaling(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    column_mean = data.mean(axis=0)
    column_std = data.std(axis=0)
    standardized_data = (data - column_mean) / column_std
    column_max = data.max(axis=0)
    column_min = data.min(axis=0)
    normalized_data = (data - column_min) / (column_max - column_min)
    return np.round(standardized_data, decimals=4), np.round(
            normalized_data, decimals=4)
