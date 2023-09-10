

class Student2:

    def sum(self, a=None, b=None, c=None):

        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
            
        return s
    
s1 = Student2()

print(s1.sum(1,2,3))

print(s1.sum(1,2))

print(s1.sum(1))