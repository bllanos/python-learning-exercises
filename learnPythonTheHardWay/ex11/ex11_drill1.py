# Trying raw_input with a prompt
a = raw_input("Follow the prompt. (That was it)")
# Here, a space is not added after the prompt.
print "You entered %r" % a

# Trying basic number input
print "Enter an integer",
stringNum = raw_input()
num = int(stringNum) # Might throw a value error.
print "You entered %s, converted to %g." % (stringNum, num)
