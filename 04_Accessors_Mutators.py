"""
Accessors are nothing but GET/Read method to read the value of that property/variable
Mutators are nothing but SET/Write method to write the value of that property/variable

OOP best practise is to write (GET and SET) methods or (ACCESSORS and MUTATORS) methods
"""

# Class Rectangle
class Rectangle(object):

    def __init__(self, length, width):
        self.length = length  # Instance variable 1
        self.width = width  # Instance variable 2

    # GET and SET method for length propertyy
    @property
    def Length(self):
        return self.length

    # If you define the setter with a different name like this it won't work
    # Example if I name GET property method as Length (line 17) then the SET property method name should also be Length (line 23)
    @Length.setter
    def Length(self, new_length):
        self.length = new_length

    # GET and SET method for width property
    @property
    def Width(self):
        return self.length

    @Width.setter
    def Width(self, new_width):
        self.length = new_width

    # Instance method 1
    def calculate_area(self):
        return self.length * self.width

    # Instance method 2
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

r1 = Rectangle(10, 10)  # r1 is an object/Instance of Class Rectangle
print(f"r1.Length : {r1.Length}")
print(f"Setting length to 20")
r1.Length = 20
print(f"r1.Length :{r1.Length}")

