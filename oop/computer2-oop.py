class Computer:

    def __init__(self):
        self.name = 'prasiddha'
        self.age = 20
    
    # using self to change the attribute of the object
    def update(self):
        self.name = 'pokhrel'
    
    #function to compare the name of two objects after changing the name from the update fn.
    def compare(self, object_to_compare):
        if self.name == object_to_compare.name:
            print('They are same')
        else:
            print('They are different')


c1 = Computer()
c2 = Computer()

# also we can change the object attribute value directly by:
# c1.name = 'sagar'

c1.update()
c1.compare(c2)