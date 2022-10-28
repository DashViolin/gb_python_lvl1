from abc import ABC, abstractmethod
from typing import Union


class Clothes(ABC):
    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        vals = {key: val for key, val in self.__dict__.items()}
        return ', '.join([f'{key}: {vals[key]}' for key in vals])

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v: Union[int, float]):
        self.v = v
        super().__init__(title='Coat')

    def tissue_consumption(self):
        return round(self.v / 6.5 + 0.5, 2)


class Costume(Clothes):
    def __init__(self, h: Union[int, float]):
        self.h = h
        super().__init__(title='Costume')

    def tissue_consumption(self):
        return round(self.h * 2 + 0.3, 2)


coat = Coat(6)
print(coat)
print(f'Tissue consumption: {coat.tissue_consumption()}')

costume = Costume(8.5)
print(costume)
print(f'Tissue consumption: {costume.tissue_consumption()}')
