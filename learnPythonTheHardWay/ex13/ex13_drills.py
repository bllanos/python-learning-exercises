from sys import argv

script, one = argv
print "Script = %s" % script
print "First command line argument =", one

others = raw_input("Add some more input: ")
print "You wrote: %s" % others
