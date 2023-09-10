'''
overriding the method of parent class in the child class
see the example below, method show of the class A is 
overriden in the class B
'''

class A:

    def show(self):
        print('show in A')


class B(A):

    def show(self):
        print('show in B')


a = A()

a.show()

b = B()

b.show()