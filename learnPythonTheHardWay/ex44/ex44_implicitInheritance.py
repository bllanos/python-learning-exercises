class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent() # Recall: no use of 'new'
son = Child()

dad.implicit()
son.implicit()
