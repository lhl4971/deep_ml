def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if (mode == "row"):
        for i in range(len(matrix)):
            arr_sum = 0
            for j in range(len(matrix[i])):
                arr_sum += matrix[i][j]
            means.append(arr_sum/len(matrix[i]))
    elif (mode == "column"):
        for i in range(len(matrix[0])):
            arr_sum = 0
            for j in range(len(matrix)):
                arr_sum += matrix[j][i]
            means.append(arr_sum/len(matrix))
    return means


def calculate_covariance_matrix(
        vectors: list[list[float]]
        ) -> list[list[float]]:
    means = calculate_matrix_mean(vectors, mode="row")
    covariance_matrix = []
    for i in range(len(means)):
        arr = []
        for j in range(len(means)):
            tmp = 0
            for k in range(len(means)):
                tmp += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
            arr.append(tmp/(len(means)-1))
        covariance_matrix.append(arr)
    return covariance_matrix
