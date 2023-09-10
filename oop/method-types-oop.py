# 4 types of methods in python
# instance method, class method, static method and dunder/special/magic method

class Student:

    school = 'prasiddha'

    def __init__(self, m1,m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    # instance method needs self as parameter
    # works with instance methods
    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3
    
    # class method needs cls as parameter and needs @classmethod as decorator
    # works with class variables
    # and can be directly accessed by class.classmethod() just like class variables and by object also.

    @classmethod
    def getSchool(cls):
        return cls.school
    

    # static method doesn't need mandatory parameter as instance and class methods,
    # it needs @staticmethod as decorator
    # they are typically used for utility functions that are related
    # to the class but don't depend on instance-specific or class-specific data.
    # they can be called by Student.staticmethod() or s1.info()

    @staticmethod
    def info(a,b):
        print('This is a static method', a+b)

s1 = Student(1,2,3)

print(s1.avg())

print(Student.getSchool())

s1.info(2,3)

#special method/magic/dunder methods.
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"MyClass instance with value: {self.value}"

obj = MyClass(42)
print(obj)  # Calls the __str__ method for string representation

