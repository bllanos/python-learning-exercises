import random

class SmallInteger(object):
    """Select a random integer from zero up to SmallInteger.MAX"""
    
    _MAX = 100
    
    # Public access is nice, but don't allow changes
    # Defining a property of a class, not an instance:
    #   http://stackoverflow.com/questions/128573/using-property-on-classmethods
    #   Python 3 syntax would be a bit different
    class __metaclass__(type):
        """Provides a MAX property for the class."""
        @property
        def MAX(cls):
            """Maximum integer value."""
            return cls._MAX
    
    def __init__(self):
        (self._value) = random.randint(0, self._MAX)
        
    def __str__(self):
        return "%d" % self._value
        
    def value(self):
        # Should use properties instead of accessor functions
        return self._value
