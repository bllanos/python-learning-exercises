print "The 'r' format character calls the 'repr()' function."
print "See https://docs.python.org/2/library/functions.html#func-repr"
print "It is like reverse quotes, but they are deprecated? (http://bugs.python.org/issue3523)"
variable = 67.2
print "variable = %r" % variable # Note: No comma between format string and the values to format
print "repr(variable) = %s" % repr(variable)
Variable = 2
print "variable == Variable ? (%s)" % (variable == Variable)
# The above statement differs from `print "variable == Variable ? (%s)" % variable == Variable`!
# which just prints 'False'

print "Variable names are case-sensitive."

myStr = "Formatted number: %d" % 73.8 # Note: Truncation
print myStr
