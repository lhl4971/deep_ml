import numpy as np


def linear_regression_normal_equation(
        X: list[list[float]], y: list[float]
        ) -> list[float]:
    X = np.array(X)
    y = np.array(y)
    t_trans_t = np.dot(X.T, X)
    t_trans_t_inv = np.linalg.inv(t_trans_t).astype(float)
    t_trans_y = np.dot(X.T, y)
    theta = np.dot(t_trans_t_inv, t_trans_y)
    return np.round(theta, decimals=4).tolist()
