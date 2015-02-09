print "I will now count my chickens:"
print 'Single quotes also work to delimit string literals.'

print "Hens", 25 + 30 / 6 # = 30
# When printing, a space is inserted between arguments.
print "Roosters", 100 - 25 * 3 % 4 # = 100 - (25 * 3) % 4
                                   # = 100 - 75 % 4
                                   # = 100 - 3 = 97
print "Now I will count", "the", "eggs:"
# print is a variadic function.
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# `%` and `/` have highest precedence here
# = 6 - 5 + 0 - 0.25 + 6
# = 6.75 (Incorrect)
# = 7, because integer division must have occured

print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7 # = 5 < -2 = false (or, specifically, 'False')

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "How about some more."

print "Is it greater?", 5 > -2 # True
print "Is it greater or equal?", 5 >= -2 # True
print "Is it less or equal?", 5 <= -2 # False
