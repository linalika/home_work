class Matrix:
    def __init__(self, *matrix):
        self.matrix = matrix

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(row1, row2)]
                       for row1, row2 in zip(*self.matrix, *other.matrix)])


matrix1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
matrix2 = Matrix([[3, 3, 3], [1, 2, 3], [5, 5, 5]])
print(matrix1 + matrix2)
