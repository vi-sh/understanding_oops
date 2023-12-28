# Class Rectangle
class Rectangle:

    def __init__(self, length, width):
        self.length = length  # Instance variable
        self.width = width  # Instance variable

    # Instance method 1
    def calculate_area(self):
        return self.length * self.width

    # Instance method 2
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    """
    Static method does NOT uses any members of instance or class variables
    Since it is somehow related to class 
    we are writing within the class to check if the object so created is a square or not   
    """
    @staticmethod
    def issquare(length, width):
        if length == width:
            print(f"Given Rectangle is a Square")
        else:
            print(f"Given Rectangle is NOT a square")


r1 = Rectangle(10, 10)  # r1 is an object/Instance of Class Rectangle

r1.issquare(r1.length, r1.width)  # Since both length and width are same here issquare() prints , Given Rectangle is a Square

