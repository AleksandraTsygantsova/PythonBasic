class Road:

    def __init__(self, length, width):
        print('Запуск программы расчета массы асфальта...')
        self._length = length
        print(f'Длина асфальтового полотна равна {self._length}')
        self._width = width
        print(f'Ширина асфальтового полотна равна {self._width}')
        print(self.weight())


    def weight(self):
        result = self._length * self._width * 25 * 5
        print(f'Масса асфальтового полотна равна {result} тонн')

my_road = Road(length=10, width=20)