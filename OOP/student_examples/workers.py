"""
Workers class example.
By Mirsolav, 2017
"""


class Workers:  # "Workers" is the class name

    def __init__(self, name, age, address, hometown):  # "__init__" is the method
        self.name = name  # ".name" (after "self") is attribute
        self.age = age
        self.address = address
        self.hometown = hometown


ivan = Workers('Ivan,', '28 years,', 'Blueberry Street 36,', 'Utopia.')  # "ivan" is the object created from the class "Workers"
josip = Workers('Josip,', '36 years,', 'Yellowlight Street 136,', 'Oz.')
miro = Workers('Miro,', '38 years,', 'Color Street 1,', 'Dreamland Town.')
blondie = Workers('Marijana,', '24 years,', 'Strawberry Street 95,', 'Bluetown.')

print(ivan.name, ivan.age, ivan.address, ivan.hometown)
print(josip.name, josip.age, josip.address, josip.hometown)
print(miro.name, miro.age, miro.address, miro.hometown)

print(blondie.name, blondie.age, blondie.address, blondie.hometown)
