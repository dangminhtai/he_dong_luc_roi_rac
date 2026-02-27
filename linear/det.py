def det2(matrix):
    """Calculate the determinant of a 2x2 matrix."""
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix.")

    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def op_det2(matrix):
    """Tính định thức đối của ma trận 2x2."""
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix.")

    return matrix[0][1] * matrix[1][0] - matrix[0][0] * matrix[1][1]
