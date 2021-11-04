from typing import List


class Matrix:
    def __init__(self, rows: List[List[int]]):
        self.__rows: list = rows
        self.cols: list = list(zip(*self.__rows))
        self.rows_count = len(self.__rows)
        self.cols_count = len(self.cols)

    @property
    def rows(self):
        return self.__rows

    @rows.setter
    def rows(self, rows):
        if len(rows) > 3 or any(map(lambda x: len(x) > 4, rows)) or max(map(len, rows)) != min(map(len, rows)):
            raise ValueError('Matrix can be only 3x2, 3x3 or 2x4.')
        self.__rows = rows

    def __str__(self):
        rows = "\n".join(map(lambda x: ',\t'.join(map(str, x)), self.__rows))
        return f'\n{rows}\n'

    def __add__(self, other: ['Matrix']) -> ['Matrix']:
        if self.rows_count != other.rows_count or self.cols_count != other.cols_count:
            raise ValueError('Matrices mus be the same size')
        res = [[item_1 + item_2 for item_1, item_2 in zip(row_1, row_2)] for row_1, row_2 in zip(self.rows, other.rows)]
        return Matrix(res)


A1 = Matrix([
    [31, 22],
    [37, 43],
    [51, 86],
])

A2 = Matrix([
    [12, 12],
    [31, 43],
    [10, 16],
])

B1 = Matrix([
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, -8],
])

B2 = Matrix([
    [3, 2, 1],
    [3, -1, 9],
    [-1, 4, -8],
])

C1 = Matrix([
    [3, 5, 8, 3],
    [8, 3, 7, 1],
])

C2 = Matrix([
    [8, 3, 7, 1],
    [3, 5, 8, 3],
])

print(A1 + A2)
print(B1 + B2)
print(C1 + C2)
