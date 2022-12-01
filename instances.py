# instnatiating a class which is a container for functions etc
class Parent(object):

    # this function prints a statement
    def altered(self):
        print('PARENT altered()')

# this class inherits the functionality of class Parent
# i can type 'pass' within this class and the functionality will remain the same
# this is good for repetitive code but bad for storing classes within variables
class Child(Parent):

    # because I have not typed 'pass' and instead defined a function
    # the inheritance will be overridden
    def altered(self):
        
        # this will still print ('PARENT altered()')
        print('CHILD, BEFORE PARENT altered()')
        
        # python's super function can overide instances
        # the .altered() fires the function that has the overridden instance
        super(Child, self).altered()
        print('CHILD, AFTER PARENT altered()')

# storing the classes as variables
dad = Parent()
son = Child()

# stating the varible and then firing the function
dad.altered()
son.altered()