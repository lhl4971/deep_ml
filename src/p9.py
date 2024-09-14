def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:
    c = []
    for i in range(len(a)):
        arr = []
        for j in range(len(b[0])):
            if len(a[i]) != len(b):
                return -1
            tmp = 0
            for k in range(len(b)):
                tmp += a[i][k]*b[k][j]
            arr.append(tmp)
        c.append(arr)
    return c
