

class Animal:
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False   # Накормленное
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    pass  # Цветы не съедобные

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
print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

print(a1.alive)  # True
print(a2.fed)    # False
a1.eat(p1)       # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)       # Хатико съел Заводной апельсин
print(a1.alive)  # False
print(a2.fed)    # True
