def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    l1 = ((a+d)+((a+d)**2-4*(a*d-b*c))**0.5)/2
    l2 = ((a+d)-((a+d)**2-4*(a*d-b*c))**0.5)/2
    return [l1, l2]
