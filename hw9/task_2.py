class Road:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calc_weight_in_tons(self, thickness: int, normal_consumption=25):
        return self._width * self._length * thickness * normal_consumption / 1000


road = Road(length=5000, width=20)
print(road.calc_weight_in_tons(thickness=5))
