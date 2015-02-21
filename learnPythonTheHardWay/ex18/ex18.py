# A function which resembles a mini script
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# The `*parameter` syntax is unecessary above
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# A function taking one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
# A function without parameters
def print_none():
    print "I got nothing."
    
print_two("First","Last")
print_two_again("First2","Last2")
print_one("First3")
print_none()
