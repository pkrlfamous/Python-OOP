class Computer():
    # In Python, the __init__ method is a special method also known as the constructor. It is used to initialize the attributes (properties or variables) of an object when an instance of a class is created. This method is called automatically when you create a new instance of a class, and it allows you to set the initial state of the object.
    
    def __init__(self, cpu, ram):
        self.cpu = cpu # it is similar to c1.cpu
        self.ram = ram # it is similar to c1.ram
    
    def config(self):
        print('config', self.cpu, self.ram)

# init fn is like constructor
# init fn is called when creating an object, so we have to pass two arguments when creating object.
# in code self is replaced by the object name, so that it know to which object the attribute to assign


com1 = Computer('i7','16')
com2 = Computer('ryzen 3', '8')

com1.config()
com2.config()