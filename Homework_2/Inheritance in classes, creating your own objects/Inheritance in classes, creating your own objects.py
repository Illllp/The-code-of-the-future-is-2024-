class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return f"Звук животного {self.species}"

class Dog(Animal):
    def make_sound(self):
        return "Гав"

class Cat(Animal):
    def make_sound(self):
        return "Мяу"

# Пример использования
dog = Dog("Рекс", "собака")
cat = Cat("Мурзик", "кот")

print(dog.make_sound())  # Выведет "Гав"
print(cat.make_sound())  # Выведет "Мяу"
