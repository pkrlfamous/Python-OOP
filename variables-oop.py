# In python there are two types of variables class variables (static) and instance variables.

# Class variables are associated with the class and can be accessed by the class name.

# Instance variable are associated with the method inside the class and we need object to access it.

class Car:

    #class variable
    wiper = 2

    def __init__(self):
        self.milage = 10
        self.company = 'Hundai'

Car.wiper = 3 # class variable is accessed by class name and update.
Car.milage = 20 # instance variable is accessed by class name too.

c1 = Car()
print(c1.milage, c1.company, c1.wiper, Car.milage) # class variable can be accessed by object as well.
