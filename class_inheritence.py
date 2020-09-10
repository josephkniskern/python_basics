class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 4

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


class Bird(Animal):
    def fly(self):
        print("fly")


cat = Mammal()
print(cat.age)
print(cat.weight)
