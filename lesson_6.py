#1.
import time
class TrafficLight:
    __color = ['red', 'yellow', 'green']
    def running(self):
        i = 0
        while i != 3:
            print((TrafficLight.__color[i]))
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(5)
            i += 1


traf = TrafficLight()
traf.running()


#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def asphalt(self):
        mass = self._length * self._width * 25 * 5 / 1000
        print(f'{round(mass)} т')

r = Road(5000, 20)
r.asphalt()


#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


p = Position('Fedia', 'Fedorov', 'Razrab', '10000000', '200000000')
p.get_full_name(), p.get_total_income()

#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('поехала')

    def stop(self):
        print('остановилась')

    def turn(self, direction):
        print(f'повернула  {direction}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость выше разрешенной")
        else:
            print("Нормальная скорость")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Скорость выше разрешенной")
        else:
            print("Нормальная скорость")


class PoliceCar(Car):
    pass

town = TownCar('Lada', 100, 'red', False)
print(town.name)
town.go()
town.show_speed()
town.turn('left')
town.turn('right')
town.stop()

print('************************************')
sport = SportCar('BMW', 100, 'red', False)
print(sport.name)
sport.go()
sport.show_speed()
sport.turn('left')
sport.turn('right')
sport.stop()
print('************************************')

work = WorkCar('Lada', 100, 'red', False)
print(work.name)
work.go()
work.show_speed()
work.turn('left')
work.turn('right')
work.stop()
print('************************************')

police = PoliceCar('Audi', 100, 'red', False)
print(police.name)
police.go()
police.show_speed()
police.turn('left')
police.turn('right')
police.stop()
print('************************************')
#5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


pen = Pen('ручкой')
pen.draw()
pencil = Pencil('карандашом')
pencil.draw()
handle = Handle('маркером')
handle.draw()