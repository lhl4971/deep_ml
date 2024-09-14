def matrix_dot_vector(
        a: list[list[int | float]], b: list[int | float]
        ) -> list[int | float]:
    c = [0 for _ in range(len(b))]
    for i in range(len(a)):
        if len(a[i]) != len(b):
            return -1
        for j in range(len(b)):
            c[i] += a[i][j]*b[j]
    return c
