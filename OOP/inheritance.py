class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage
        print("{} attacks {}!".format(self.name, other_guy.name))
        print("{} loses {} health points!".format(other_guy.name, self.damage))

    def __str__(self):
        return "{}: {}".format(self.name, self.health)

qazi = Fighter("Qazi")
you = Fighter("Matt")

print(qazi)  # Qazi: 100
print(you)

you.attack(qazi)
print(qazi)

class Boxer(Fighter):
    def heal(self):
        self.health += 10


boxer_qazi = Boxer("Boxer Qazi")
print(boxer_qazi)
print(boxer_qazi.damage)
print(boxer_qazi.health)

boxer_qazi.heal()

print(boxer_qazi)
