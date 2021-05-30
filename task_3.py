class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count > other.count:
            return Cell(self.count - other.count)

            # raise ValueError(f"{self._count} - {other._count}: impossible operation")
        print(f"{self.count} - {other.count}: impossible operation")

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, per_row: int) -> str:
        rows, tail = self.count // per_row, self.count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self.count} ячеек"


c1 = Cell(17)
print(c1)
c2 = Cell(13)
print(c2)

print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)
print((c1 * c2).make_order(23))
