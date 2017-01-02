class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

pet_qazi = Animal("Qazoo")
print(pet_qazi.name)
print(pet_qazi.talk())

class Dog(Animal):
    def talk(self):
        return "WOOF"


pet = Dog("Dot")
print(pet.name)
print(pet.talk())

class Cat(Animal):
    def talk(self):
        return "Meow"


kitten = Cat("Brian")
print(kitten.name)
print(kitten.talk())
