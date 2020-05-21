import time

class TrafficLight:
    def __init__(self):
        print('Запускаем программу светофора...')
        self.__color = 'красный'

    def running(self):
        self.__color = 'красный'
        print(f'Загорелся {self.__color} свет')
        time.sleep(7)

        self.__color = 'желтый'
        print(f'Загорелся {self.__color} свет')
        time.sleep(2)

        self.__color = 'зеленый'
        print(f'Загорелся {self.__color} свет')
        time.sleep(5)

        while True:
            self.running()

a = TrafficLight()
print(a.running())