class Matrix:
    def __init__(self, a, b, c, x, y, z, q, w, e):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y
        self.z = z
        self.q = q
        self.w = w
        self.e = e
        self.list = [[a, b, c], [x, y, z], [q, w, e]]

    def __str__(self):
        return f'{self.a} {self.b} {self.c}\n{self.x} {self.y} {self.z}\n{self.q} {self.w} {self.e}\n'


    def __add__(self, other):
        return Matrix(self.list[0][0] + other.list[0][0], self.list[0][1] + other.list[0][1], self.list[0][2] + other.list[0][2],
                      self.list[1][0] + other.list[1][0], self.list[1][1] + other.list[1][1], self.list[1][2] + other.list[1][2],
                      self.list[2][0] + other.list[2][0], self.list[2][1] + other.list[2][1], self.list[2][2] + other.list[2][2])

a = Matrix(6, 7, 8, 9, 10, 11, 5, 4, 3)
b = Matrix(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a)
print(b)

print(a + b)