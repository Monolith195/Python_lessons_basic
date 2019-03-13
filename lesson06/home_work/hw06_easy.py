# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("{} поехала".format(self.name))

    def stop(self):
        print("{} остановилась".format(self.name))

    def turn(self, direction):
        print("{} повернула {}".format(self.name, direction))


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
