# class inside a class
# can create inneer class object inside outer class
# can create inner class object outside outer class


class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.l1 = self.Laptop()  # create object of inner class using self

    def show(self):
        print(self.name, self.rollno)
        self.l1.show() # calling inner class Laptop class's method inside another method

    class Laptop:

        def __init__(self):
            self.brand = 'dell'
            self.processor = 'i7'

        def show(self):
            print(self.brand, self.processor)

s1 = Student('prasiddha', 1)

lap1 = Student.Laptop() # creating inner class's obj outside outer class.

s1.show()

print(s1.l1.brand) # printing attributes of inner class calling by it's object

print(lap1.brand) # printing attributes of inner class calling by it's object
