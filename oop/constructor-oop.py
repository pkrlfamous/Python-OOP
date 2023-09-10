class A:

    def __init__(self):
        print('init in A')
    
    def feature1(self):
        print('Feature 1 working')



class B(A):  # extending class A so that we can access the methods of the class A

    def __init__(self):
        super().__init__() # using super keyword to access init method of superclass
        print('init in B')

    def feature2(self):
        print('Feature 2 working')


a1 = B() # init function of class b is called.


'''Method resolution order
in multiple inheritance init of the left hand side of the super class is called
when creating object of the subclass, this is called Method resolution order'''

class A:

    def __init__(self):
        print('init in A')
    
    def feature1(self):
        print('Feature 1 working')



class B:  # extending class A so that we can access the methods of the class A

    def __init__(self):
        super().__init__() # using super keyword to access init method of superclass
        print('init in B')

    def feature2(self):
        print('Feature 2 working')


class C(A, B): # MRO is used here

    def __init__(self):
        super().__init__()
        print('init in C')
    

    def feat(self):
        super().feature2() # using super to call method of super/parent class

c1 = C()
c1.feat()