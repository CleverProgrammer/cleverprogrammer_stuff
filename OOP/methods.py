class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage


qazi = Fighter("Qazi")
you = Fighter("Matt")

print(qazi.name)
print(you.name)

you.attack(qazi)
print(qazi.health)
