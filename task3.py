class Worker:

    _income = {'wage': 'wage', 'bonus': 'bonus'}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

class Position (Worker):
    def get_full_name(self):
        full_name = self.name + self.surname
        print(full_name)
    def get_total_income(self):
        # total_income = self._income + (self._income * 0.2)
        total_income = self._income['wage'] + self._income['bonus']

        print(f'Доход сотрудника с учетом премии составил: {total_income} руб.')

a = Position(name='Alex', surname='Bowie', position='manager', wage=20000, bonus=4000)
a.get_full_name()
a.get_total_income()