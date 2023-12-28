# Class Rectangle
class Rectangle:

    count = 0  # class variable
    
    """
    Constructor : This is called when an Object/Instance of a Class is created.
    Self is an Instance itself
    """
    def __init__(self, length, width):
        self.length = length  # Instance variable
        self.width = width  # Instance variable
        Rectangle.count += 1

    """
    Instance Method : A method that uses Instance variables
    """
    # Instance method 1
    def calculate_area(self):
        return self.length * self.width

    # Instance method 2
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    """
    Class Method : A method that uses Class variables
    """
    @classmethod  # annotation to make the method as Class method
    def count_rectangle_objects(cls):  # Cls is the Class variable which is the class itself
        return cls.count


r1 = Rectangle(10, 5)  # r1 is an object/Instance of Class Rectangle
print(f"Objects created so far : {Rectangle.count}")  # It will print 1 since only 1 object r1 is created at this moment
r2 = Rectangle(12, 3)  # r2 is an object/Instance of Class Rectangle
"""
Both r1 and r2 will have there own Instance variables and Instance methods that is
- r1 (r1 itself will be its own self) will have its own length and width and its own calculate_area() and calculate_perimeter()
- r2 (r2 itself will be its own self) will have its own length and width and its own calculate_area() and calculate_perimeter()
"""

print(f"Objects created so far : {Rectangle.count}")  # It will print 2 since 2 objects r1 and r2 are created at this moment

"""
You can call the count_rectangle_objects by the object and also by the class ,
This confirms that class variable and class methods are accessible by both the class and its objects/instances
"""

print(f"Printing count of objects created by object r1.count_rectangle_objects() : {r1.count_rectangle_objects()}")
print(f"Printing count of objects created by object r2.count_rectangle_objects() : {r2.count_rectangle_objects()}")
print(f"Printing count of objects created by class Rectangle.count : {Rectangle.count}")
