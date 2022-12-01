class Parent(object):

    def override(self):
        print('PARENT overide()')

    def implicit(self):
        print('PARENT implicit()')

    def altered(self):
        print('PARENT altered()')

class Child(Parent):

    def override(self):
        print('CHILD override()')
    
    def altered(self):
        print('CHILD, BEFORE PARENT altered()')
        super(Child, self).altered()
        print('CHILD, AFTER PARENT altered()')

dad = Parent()
son = Child()

# not overriden
dad.implicit()

# inherited 
son.implicit()

# not overriden
dad.override()

# overridden
son.override()

# not overridden 
dad.altered()

# overriden
son.altered()