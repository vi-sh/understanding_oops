"""
A class can extend another class, The original class is called PARENT class and
the class that extends the Parent class is called CHILD class.

The CHILD class can inherit all the properties and methods of the PARENT class. This is called INHERITANCE.
"""

class Dog:  # Parent class

    _legs = 4  # class variable which is common for all instances of Dog

    def __init__(self, name):  # Parent class constructor
        self.name = name

    def bark(self):     # Parent class method
        print(f"{self.name} says: BoW! BoW!")

    def getLegs(self):  # Parent class method
        print(f"{self.name} has {self._legs} legs")

class Rottweiler(Dog):  # my_rottweiler is a child class of Dog

    def __init__(self, name):  # Child class constructor

        """
        super() is used to call the constructor of the parent class Dog
        This super() will call the constructor of the parent class Dog and pass the name to it
        """
        super().__init__(name)

    def bark(self):  # Child class method overriding the parent class method
        print(f"{self.name} says: Grrr! Grrr!")

my_rottweiler = Rottweiler("Bruno")  # Creating an object of the child class my_rottweiler

print("-----------------------------")
print("This will call the bark() method of the child class Rottweiler\n"
      "Since it is overridden in the child class Rottweiler"
      "bark() method of the Child class is called and prints Grrr! Grrr! instead of BoW! BoW!")
print("---------------------------------------------------------------------------------------")
my_rottweiler.bark()

print("-----------------------------")
print("This will call the getLegs() method of the parent class Dog\n"
      "since it is moslty common for all Dogs to have 4 legs, we made it as class variable\n"
      "which is common for all instances of Dog and not specific to any instance of Dog\n")
print("---------------------------------------------------------------------------------------")
my_rottweiler.getLegs()
