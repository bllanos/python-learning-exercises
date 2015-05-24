import random

class SmallInteger(object):
    """Select a random integer from zero up to SmallInteger.MAX"""
    
    MAX = 100
    
    def __init__(self):
        (self._value) = random.randint(0, self.MAX)
        
    def __str__(self):
        return "%d" % self._value
        
    def value(self):
        # Should use properties instead of accessor functions
        return self._value
