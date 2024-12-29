class Animal:
    def speak(self):
        print('Животное говорит')

animal = Animal()
animal.speak()

print('--------------------------------')

class Dog(Animal):
    def speak(self):
        print('гав-гав')

dog = Dog()
dog.speak()

print('--------------------------------')

class Big_Dog(Animal):
    def speak(self):
        print('Большой гав-гав')


class Small_Dog(Animal):
    def speak(self):
        print('Маленький гав-гав')

bobick = Big_Dog()
bobick.speak()

print('--------------------------------')

sharick = Small_Dog()
sharick.speak()

print('--------------------------------')

class Toy_Dog(Small_Dog):
    def speak(self):
        print('Игрушечный гав-гав')

toy = Toy_Dog()
toy.speak()

print('--------------------------------')

class BigAngryDog(Big_Dog):
    def speak(self):
        print('Большой гав-гав с гневом')
        super().speak()  # вызывает метод, который вызывается после (вызывается без self())
        print('Хмурится')

tusick = BigAngryDog()
tusick.speak()

print('--------------------------------')

class Cat(Animal):
    def _meow(self): # _ защищенный метод
        print('Мяу')
    def speak(self):
        self._meow()

tom = Cat()
tom.speak()

print('--------------------------------')

class newcat(Cat):
    def _meow(self):
        print('shhhh')

newCat = newcat()
newCat.speak()

print('--------------------------------')

def say_n_times(animal, times):
    for _ in range(times):
        animal.speak()

druzock = BigAngryDog()
say_n_times(druzock, 2)

print('--------------------------------')

list_of_animals = [Cat(), Dog(), BigAngryDog()]
for animal in list_of_animals:
    animal.speak()