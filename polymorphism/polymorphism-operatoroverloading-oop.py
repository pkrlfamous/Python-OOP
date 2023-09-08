a, b = 5, 6

print(a + b)

print(int.__add__(a,b))

if a > b:
    pass

'''
Operator overloading allows you to define your own custom behavior for built-in operators such as +, -, *, and so on, by implementing special methods like __add__, __sub__, and others in your classes. These special methods are used to define how instances of your class should behave when these operators are applied to them. This enables you to customize the behavior of operators for objects of your class, making your code more expressive and intuitive.
'''
# we defined our own add function
# if we need to add two objects we need to overload add operator, 
# we need to define our __add__ fn instead of using built it __add__ fn

class Student:

    def __init__(self, m1, m2):
        self.n1 = m1
        self.n2 = m2

    def __add__(self, other): # evaluates to Student.__add__(s1, s2) s1 replaces 'self' of the add fn and s2 replaces to 'other' of the add fn.
        o1 = self.n1 + other.n1 # we are able to add the attributes of two diff fns
        o2 = self.n2 + other.n2
        s3 = Student(o1, o2)
        return s3


    '''
    overloading python default greater than operator with our custom code.
    '''
    def __gt__(self, other):
        p1 = self.n1 + self.n2
        p2 = other.n1 + other.n2

        if p1 > p2:
            return True
        else:
            return False

s1 = Student(99, 100)
s2 = Student(99, 101)



s3 = s1 + s2 # evaluates to Student.__add__(s1, s2) s1 replaces self of the add fn and s2 replaces to 'other' of the add fn.

print(s3.n1)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')
