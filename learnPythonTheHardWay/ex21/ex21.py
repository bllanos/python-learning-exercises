def add(a, b):
    print "ADDING %d + %d" % (a, b)
    # a + b # This returns a result of type NoneType
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# = ... 25
# = ... 180 * 25
# = ... 3600 + 900
# = ... 4500
# = ... 74 - 4500
# = ... -4426
# = 35 - 4426
# = -4391 (correct)
print "That becomes: ", what

def noReturn():
    0
print "No return value is %r" % noReturn() # None
