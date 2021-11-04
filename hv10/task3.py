class Cells:
    def __init__(self, cells_count: int, cells_char: str = '*'):
        if cells_count <= 0:
            raise ValueError('cells_count must be positive.')
        self.cells_count = cells_count
        self.cells_char = cells_char

    def __add__(self, other):
        return Cells(self.cells_count + other.cells_count)

    def __sub__(self, other):
        sub = self.cells_count - other.cells_count
        if sub <= 0:
            raise ValueError('subtraction result must be positive.')
        return Cells(sub)

    def __mul__(self, other):
        return Cells(self.cells_count * other.cells_count)

    def __truediv__(self, other):
        return self.__floordiv__(other)

    def __floordiv__(self, other):
        return Cells(self.cells_count // other.cells_count)

    def __str__(self, cells_in_row: int = 5):
        return self.make_order(cells_in_row)

    def make_order(self, cells_in_row):
        def chunker(seq, size):
            return (seq[pos:pos + size] for pos in range(0, len(seq), size))

        cells = self.cells_count * self.cells_char
        return '\n'.join(chunker(cells, cells_in_row))


cell_1 = Cells(8)
cell_2 = Cells(3)
print(cell_1, end='\n\n')
print(cell_2, end='\n\n')
print(cell_1 + cell_2, end='\n\n')
print(cell_1 - cell_2, end='\n\n')
print((cell_1 * cell_2).make_order(12), end='\n\n')
print(cell_1 // cell_2, end='\n\n')
print(cell_1 / cell_2, end='\n\n')
