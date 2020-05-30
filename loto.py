import random


class Game:
    def __init__(self, name):
        print(f'Welcome to a game {name}')
        self.card = self.generate_cards()
        self.barrel = self.generate_barrel()
        self.compcard = self.generate_cards()

        if input('To start the game press S:\n>> ') == 's' or 'S': self.start_game()

    def generate_cards(self):
        numbers = list(range(1, 91))
        random.shuffle(numbers)
        card_numbers = list(sorted(numbers[0:27]))

        final_card_numbers = []
        circle = 0

        while len(card_numbers) > 0:
            numbers_to_delete = list(range(0, 8))
            random.shuffle(numbers_to_delete)
            delete_list = list(numbers_to_delete[0:4])

            for i in delete_list:
                card_numbers[i] = '_'

            final_card_numbers.append(card_numbers[0:9])

            for x in final_card_numbers[circle]:
                card_numbers.remove(x)

            circle += 1

        return final_card_numbers

    def generate_barrel(self):
        numbers = list(range(1, 91))
        random.shuffle(numbers)
        current_number = numbers[0]
        numbers.remove(current_number)
        return current_number


    def start_game(self):
        self.barrel = self.generate_barrel()
        print(f'New barrel is: {self.barrel}')
        print(f'Your card:')
        for row in self.card:
            print(row)

        print(f'Computer card:')
        for row in self.compcard:
            print(row)

        next_move = input('Do you have same number in card? Press Yes (Y) or No (N):')
        if next_move == 'No' or next_move == 'n' or next_move == 'no' or next_move == 'N':
            self.comp_move()
        else:
            self.player_move()


    def player_move(self):
        breaknum = 0
        for row in self.card:
            if self.barrel not in row:
               breaknum += 1
            else:
                breaknum = 0

        if breaknum == 3: return print('Game over')

        for row in self.card:
            if self.barrel in row:
                row.remove(self.barrel)

        self.comp_move()

    def comp_move(self):

        print('xxx')
        for row in self.compcard:
            if self.barrel in row:
                row.remove(self.barrel)
            else:
                print('\n')

        self.start_game()


player = Game('Alex')


