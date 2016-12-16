class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age


kitty = Student('Kitty', 85, 30)
daniel = Student('Daniel', 80, 15)

print(kitty.name)
print(daniel.name)

print(kitty.grade)
print(daniel.grade)

print(kitty.age)
print(daniel.age)