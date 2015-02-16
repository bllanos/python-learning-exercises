from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C) or CTRL-D (^D)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') # Open for writing
# target.truncate() # Truncate to zero size
# This happens automatically anyway
# since the file is opened with the 'w' flag.

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()
