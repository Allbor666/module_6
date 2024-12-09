
import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # Изначальные координаты
        self.speed = speed

    def move(self, dx, dy, dz):
        # Изменяем координаты с учетом скорости
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed

        # Меняем координату z с проверкой условия
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")


class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True  # Наличие клюва

    def lay_eggs(self):
        eggs_number = random.randint(1, 4)  # Случайное число от 1 до 4
        print(f"Here are {eggs_number} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3  # Уровень опасности для водных животных

    def dive_in(self, dz):
        dz = abs(dz)  # Берем значение по модулю
        new_z = self._cords[2] - dz * (self.speed / 2)  # Скорость при нырянии пополам
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] = new_z


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8  # Уровень опасности для ядовитых животных


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"  # Звук утконоса

    def speak(self):
        print(self.sound)


# Пример использования
db = Duckbill(10)

# Проверка атрибутов утконоса
print(db.live)  # True
print(db.beak)  # True

# Проверка методов
db.speak()  # Click-click-click
db.attack()  # Be careful, I'm attacking you 0_0

# Передвижение и получение координат
db.move(1, 2, 3)  # Передвижение утконоса
db.get_cords()  # X: 10 Y: 20 Z: 30

# Ныряние
db.dive_in(6)  # Уменьшает Z на 3 (6/2)
db.get_cords()  # Проверка текущих координат

# Откладывание яиц
db.lay_eggs()  # Здесь будет вывод случайного количества яиц
