class Stationery:
    def __init__(self, title):
        pass
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Идет процесс отрисовки ручкой...')
class Pencil(Stationery):
    def draw(self):
        print('Идет процесс отрисовки карандашом...')
class Handle(Stationery):
    def draw(self):
        print('Идет процесс отрисовки маркеромы...')

a = Pen(title= 'Text')
a.draw()