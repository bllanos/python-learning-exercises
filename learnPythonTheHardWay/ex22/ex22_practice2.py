# Trying the exponentiation operator
two = 2
result = two ** 2
print "two ** 2 =", result
result **= 2
print "... ** 2 =", result
print "2 ** 32 - 1 =", 2 ** 32 - 1
print "2 ** 32 =", 2 ** 32
print "2 ** 64 - 1 =", 2 ** 64 - 1
print "2 ** 64 =", 2 ** 64
# Python does not have integer overflow
# http://stackoverflow.com/questions/9860588/maximum-value-for-long-integer
