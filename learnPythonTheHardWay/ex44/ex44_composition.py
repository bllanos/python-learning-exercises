class Other(object):

    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER implicit()"
        
    def altered(self):
        print "OTHER altered()"
        
class Child(object):

    # A `__init__()` function is necessary
    # when the class has data attributes
    def __init__(self):
        self.other = Other() # Recall: no 'new' keyword
        
    def implicit(self):
        # Explicit, strictly speaking, whereas with inheritance
        # this really is implicit delegation of functionality
        self.other.implicit()
        
    def override(self):
        print "CHILD override()"
        
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"
        
son = Child()

son.implicit()
son.override()
son.altered()
