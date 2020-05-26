class Cell:
    def __init__(self, qty):
        self.qty = int(qty)

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        return self.qty - other.qty if (self.qty - other.qty) > 0 else print('Результат отрицательный')

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __truediv__(self, other):
        return Cell(self.qty // other.qty)


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.qty / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.qty % cells_in_row)}'
        return row

cells1 = Cell(12)
cells2 = Cell(3)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(12))
print(cells1.make_order(3))
print(cells1 / cells2)