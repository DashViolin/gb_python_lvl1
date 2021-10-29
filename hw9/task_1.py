from time import sleep
import colorama

colorama.init()


class TrafficLight:
    __color = 'RED'
    __timelapse = 7

    def __switch(self):
        # Проверка порядка переключения не нужна, так как порядок переключения гарантирован.
        if self.__color == 'RED':
            self.__color = 'YELLOW'
            self.__timelapse = 2
        elif self.__color == 'YELLOW':
            self.__color = 'GREEN'
            self.__timelapse = 5
        elif self.__color == 'GREEN':
            self.__color = 'RED'
            self.__timelapse = 7

    def run(self):
        while True:
            print(self)
            sleep(self.__timelapse)
            self.__switch()

    def __str__(self):
        term_color = getattr(colorama.Fore, f'LIGHT{self.__color.upper()}_EX')
        return f'{term_color}{self.__color}'


tl = TrafficLight()
tl.run()
