class Car:

    # class attribute
    wheels = 4

    # initializer / instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

    # method 1
    def showDescription(self):
        print("This car is a", self.color, self.style)

    # method 2
    def changeColor(self, color):
        self.color = color

c = Car('Black', 'Sedan')

# call method 1
c.showDescription()      # This car is a Black Sedan

# call method 2 and set color
c.changeColor('White')

c.showDescription()      # This car is a White Sedan

# Deleting a Attributes
del c.color

# Deleting an Object
del c