def scalar_multiply(
        matrix: list[list[int | float]], scalar: int | float
        ) -> list[list[int | float]]:
    result = []
    for i in range(len(matrix)):
        arr = []
        for j in range(len(matrix[i])):
            arr.append(matrix[i][j]*scalar)
        result.append(arr)
    return result
