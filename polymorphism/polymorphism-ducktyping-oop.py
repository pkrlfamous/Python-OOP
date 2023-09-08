
'''
Polymorphism: One method with different outputs, when called by different objects.
'''

'''
Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.
'''

class PrintLength:

    def __len__(self):
        return 9504

my_str = "Hello World"
my_list = [34, 54, 65, 78]
my_dict = {"one": 123, "two": 456, "three": 789}

printLength = PrintLength()

print(len(printLength))

print(len(my_str))

print(len(my_list))

print(len(my_dict))

'''
we are using len method without or irrrespective of it's argument type, and we are able to get the length.
python's built in function len also is an example of ducktyping, it returns the result irrespective of it's type
but the method should be there, otherwise it would create error.
'''

class Pycharm:

    def execute(self):
        print('Compiling')
        print('Running')


class MyEditor:

    def execute(self):
        print('Spelling check')
        print('Convention check')
        print('Compiling')
        print('Running')


class Laptop:

    def code(self, ide):
        ide.execute()


pyCharm = Pycharm()

myEditor = MyEditor()

l1 = Laptop()

l1.code(pyCharm)

l1.code(myEditor)