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
