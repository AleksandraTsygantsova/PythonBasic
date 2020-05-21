class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool


    def go(self):
        dir = input('Choose the side to go: print F to go forward, print B to go backward >> ')
        if dir == 'F' or dir == 'f': print('Your car goes forward')
        elif dir == 'B' or dir == 'b': print('Your car goes backward')
        else: print('Incorrect command. Try again. Choose the side to go: print F to go forward, print B to go backward')

    def stop(self):
        print('Your car has been stopped')

    def turn_direction(self):
        dir = input('Choose the side to turn: print L to go left, print R to go right >> ')
        if dir == 'L' or dir == 'l':
            print('Your car goes left')
        elif dir == 'R' or dir == 'r':
            print('Your car goes right')
        else:
            print('Incorrect command. Try again. Choose the side to turn: print L to go left, print R to go right')

    def show_speed(self):
        print(f'Your current speed is {self.speed} km/h')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print ('Your speed is too high')
        else:
            print(f'Your current speed is {self.speed} km/h')
class SportCar(Car):

    def turn_s_mode(self):
        print('Sport mode is on.')

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Your speed is too high')
        else:
            print(f'Your current speed is {self.speed} km/h')

class PoliceCar(Car):

    def sirene_signal(self):
        print('Sirene in os.')


c = TownCar(speed=90, color='beige', name='Toyota', is_police=True)
c.go()
c.stop()
c.turn_direction()
c.show_speed()