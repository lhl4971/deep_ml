import numpy as np


def linear_regression_gradient_descent(
        X: np.ndarray, y: np.ndarray, alpha: float, iterations: int
        ) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    for _ in range(iterations):
        err = np.dot(X, theta) - y.reshape((3, 1))
        theta = (theta.T - alpha / m * np.dot(err.T, X)).T
    return np.round(theta, decimals=4)
