def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    b = [[0 for _l in range(len(a))] for _w in range(len(a[0]))]
    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j] = a[j][i]
    return b
