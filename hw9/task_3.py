from typing import Union


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: Union[int, float], bonus: Union[int, float]):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus,
        }

    def __str__(self):
        return f'{self.name} {self.surname} ({self.position})'


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


welder = Position(name='Alex', surname='Murphy', position='welder', wage=120000, bonus=30000)
print(welder)
print(welder.get_full_name())

miller = Position(name='Anne', surname='Lewis', position='miller', wage=150000, bonus=24000)
print(miller)
print(miller.get_total_income())
