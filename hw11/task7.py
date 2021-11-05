from typing import Union


class ComplexNum:
    def __init__(self, re: Union[int, float], im: Union[int, float]):
        self.re = re
        self.im = im

    def __str__(self):
        re = str(self.re) if self.re else ''
        im = f'{self.im}i' if self.im else ''
        if im and not im.startswith('-'):
            im = '+' + im
        return f'{re}{im}'

    def __add__(self, other: ['ComplexNum']):
        return ComplexNum(re=self.re + other.re, im=self.im + other.im)

    def __sub__(self, other: ['ComplexNum']):
        return ComplexNum(re=self.re - other.re, im=self.im - other.im)

    def __mul__(self, other: ['ComplexNum']):
        return ComplexNum(re=self.re * other.re - self.im * other.im, im=self.im * other.re + self.re * other.im)

    def __truediv__(self, other: ['ComplexNum']):
        re = (self.re * other.re + self.im * other.im) / (other.re ** 2 + other.im ** 2)
        im = (self.im * other.re - self.re * other.im) / (other.re ** 2 + other.im ** 2)
        return ComplexNum(re=re, im=im)


cn1 = ComplexNum(8, -1)
cn2 = ComplexNum(-7, 1)
print((cn1 + cn2))
print((cn1 - cn2))
print((cn1 * cn2))
print((cn1 / cn2))
