print "How old are you?", # A space is added before the input.
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (
    age, height, weight)
# Raw input is collected as strings.
