import numpy as np


def cross_validation_split(data: np.ndarray, k: int, seed=42) -> list:
    np.random.seed(seed)
    np.random.shuffle(data)
    arr_length = len(data)
    fold_length = arr_length // k

    folds = []
    for i in range(k):
        train_set_1 = data[:i*fold_length]
        train_set_2 = data[(i+1)*fold_length:]
        if i == k-1:
            train_set = train_set_1
        else:
            train_set = np.concatenate((train_set_1, train_set_2), axis=0)
        if i == k-1:
            test_set = data[i*fold_length:]
        else:
            test_set = data[i*fold_length:(i+1)*fold_length]
        folds.append([train_set.tolist(), test_set.tolist()])
    return folds
