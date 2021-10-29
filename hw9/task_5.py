class Stationery:
    title = 'канцелярская принадлежность'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'ручка'

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        print('Запуск отрисовки маркером')


stationery = Stationery()
stationery.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
