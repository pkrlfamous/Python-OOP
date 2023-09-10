
'''
single level inheritance when one class extends another class only
'''
class A:

    def feature1(self):
        print('Feature 1 working')



class B(A):  # extending class A so that we can access the methods of the class A

    def feature2(self):
        print('Feature 2 working')


a1 = A()

b1 = B()

# 
b1.feature1()
b1.feature2() # methods of the superclass/parent accessed by object of child/sub class


''' 
multi level inheritance when first class is extended by second class
 and second class is accessed by third class for example:
 A is extended by B and B by C
 A -> B -> c'''

class A:

    def feature1(self):
        print('Feature 1 working')


class B(A):  # extending class A so that we can access the methods of the class A

    def feature2(self):
        print('Feature 2 working')


class C(B):

    def feature3(self):
        print('Feature 3 working')


c1 = C()

# 
c1.feature1()
c1.feature2() # methods of the superclass/parent accessed by object of child/sub class
c1.feature3()


'''multipule inheritance
 when a class inherits multiple classes at once'''

# C inherits A and B at once.
class A:

    def feature1(self):
        print('Feature 1 working')


class B:  # extending class A so that we can access the methods of the class A

    def feature2(self):
        print('Feature 2 working')


class C(A, B):

    def feature3(self):
        print('Feature 3 working')


c1 = C()

c1.feature1()
c1.feature2() # methods of the superclass/parent accessed by object of child/sub class
c1.feature3()