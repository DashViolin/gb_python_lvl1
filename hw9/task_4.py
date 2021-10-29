from random import choice

directions = ['лево', 'право']


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __str__(self):
        police = ' (Полиция)' if self.is_police else ''
        return f'{self.color} {self.name}{police}, скорость: {self.speed}'

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Стоим.')

    def turn(self, direction):
        print(f'Поворачиваем на{direction}...')

    def show_speed(self):
        print('Текущая скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        message = f'{self.speed}' if self.speed <= 60 else f'{self.speed} (Внимание! Скорость превышена.)'
        print('Текущая скорость:', message)


class WorkCar(Car):
    def show_speed(self):
        message = f'{self.speed}' if self.speed <= 40 else f'{self.speed} (Внимание! Скорость превышена.)'
        print('Текущая скорость:', message)


police_car = Car(name='Ford Focus', color='белый', speed=100, is_police=True)
print(police_car)
police_car.show_speed()
print()
some_car = Car(name='Kia Rio', color='черный', speed=70)
print(some_car)
some_car.show_speed()
print()
working_car = WorkCar(name='Kamaz', color='оранжевый', speed=50)
print(working_car)
working_car.show_speed()
print()
town_car = TownCar(name='Lada Kalina', color='жёлтый', speed=80)
print(town_car)
town_car.go()
town_car.show_speed()
town_car.turn(choice(directions))
town_car.turn(choice(directions))
town_car.turn(choice(directions))
town_car.turn(choice(directions))
town_car.stop()
