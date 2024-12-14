import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color  # Цвет фигуры в формате RGB
        self.filled = False  # По умолчанию незакрашенная фигура
        self.__sides = []  # Список сторон

        # Проверка на количество переданных сторон
        if not self.__is_valid_sides(*sides):
            self.__sides = [1] * self.sides_count  # Заполнить единицами при ошибке
        else:
            self.__sides = list(sides)

    def __is_valid_color(self, r, g, b):
        # Проверка на корректность цвета
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        # Установка цвета с проверкой
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_color(self):
        # Возврат цвета
        return self.__color

    def __is_valid_sides(self, *new_sides):
        # Проверка корректности сторон
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        # Возврат списка сторон
        return self.__sides.copy()

    def __len__(self):
        # Возврат периметра фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        # Установка новых сторон
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        # Инициализация с длиной окружности
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * math.pi)  # Расчет радиуса

    def get_square(self):
        # Вычисление площади круга
        return math.pi * (self.__radius ** 2)

    def set_sides(self, circumference):
        # Установка стороны (длину окружности)
        super().set_sides(circumference)
        self.__radius = circumference / (2 * math.pi)  # Пересчет радиуса


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        # Инициализация с тремя сторонами
        super().__init__(color, *sides)

    def get_square(self):
        # Площадь по формуле Герона
        s = sum(self.get_sides()) / 2
        return math.sqrt(s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge_length):
        # Инициализация с 12 одинаковыми сторонами
        super().__init__(color, *([edge_length] * self.sides_count))

    def get_volume(self):
        # Возвращение объема куба
        return self.get_sides()[0] ** 3


# Пример использования:

if __name__ == "__main__":
    # Создание объектов Circle и Cube
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов
    circle1.set_color(55, 66, 77)  # Цвет изменится
    print(circle1.get_color())  # Ожидаемый вывод: (55, 66, 77)

    cube1.set_color(300, 70, 15)  # Цвет не изменится
    print(cube1.get_color())  # Ожидаемый вывод: (222, 35, 130)

    # Проверка на изменение сторон
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())  # Ожидаемый вывод: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

    circle1.set_sides(15)  # Сторона изменится
    print(circle1.get_sides())  # Ожидаемый вывод: [15]

    # Проверка периметра (круга), это длина
    print(len(circle1))  # Ожидаемый вывод: 15

    # Проверка объёма (куба)
    print(cube1.get_volume())  # Ожидаемый вывод: 216


