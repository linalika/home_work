from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def sum(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def sum(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def sum(self):
        return round(self.height * 2 + 0.3, 2)


coat = Coat(42)
costume = Costume(1.8)
print(f'Для пошива пальто потребуется {coat.sum} ткани ')
print(f'Для пошива костюма потребуется {costume.sum} ткани ')
