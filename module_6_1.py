

class Animal:
    alive = True  # Живое (классовый атрибут)
    fed = False    # Накормленное (классовый атрибут)

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность (по умолчанию)
        self.name = name


class Mammal(Animal):
    pass  # Млекопитающие используют метод eat из Animal


class Predator(Animal):
    pass  # Хищники используют метод eat из Animal


class Flower(Plant):
    pass  # Цветы являются несъедобными (по умолчанию)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты съедобные


# Создание объектов классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка состояния объектов и выполнение методов
print(a1.name) # Волк с Уолл-Стрит
print(p1.name) # Цветик семицветик

# Изначальное состояние
print(a1.alive) # True
print(a2.fed) # False

# Животные пытаются поесть
a1.eat(p1)      # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)      # Хатико съел Заводной апельсин

# Проверка состояния после еды
print(a1.fed)    # False (так как не поел)
print(a2.fed)    # True (так как поел)
