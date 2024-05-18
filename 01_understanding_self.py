class Rectangle:
    count = 0  # class variable
    """
    Constructor : This is called when an Object/Instance of a Class is created.
    Self is an Instance itself
    """

    def __init__(self, length, width):
        self.length = length  # Instance variable
        self.width = width  # Instance variable
        print(f"ID of self : {id(self)}")

    # Instance method 1
    def calculate_area(self):
        return self.length * self.width

    # Instance method 2
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


r1 = Rectangle(10, 5)  # r1 is an object/Instance of Class Rectangle

print(f"ID of r1 : {id(r1)}")

"""
When the object r1 is created it will call the constructor __init__() and prints the id(self)
and later prints id(r1) , In this case both id(self) and id(r1) is same.

so self is nothing but the object itself
"""



