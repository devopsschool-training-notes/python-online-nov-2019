"""
Create a Class
    Class Attribute
    The __init__() Method
        The self Parameter
    Methods
        Method1 - ie. CREATE
            Instance Attribute
            Instance Attribute
        Method2 - ie. READ
            Instance Attribute
            Instance Attribute
        Method3 - ie. UPDATE
            Instance Attribute
            Instance Attribute
        Method3 - ie. DELETE
            Instance Attribute
            Instance Attribute
"""

class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

# Calling a Class and it would create OBJECT
c = Car('Sedan', 'Black')
d = Car('Maruti', 'Blue')

# Access attributes
print(c.style)      # Sedan
print(c.color)      # Black

# Access attributes
print(d.style)      # Sedan
print(d.color)      # Black