from sys import argv
# This may be discouraged - See 'pydoc os.path'?
from os.path import exists as myExists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# Apparently, this causes Python to close the file
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % myExists(to_file)
print "Ready, hit RETURN to continue, CTRL-C or CTRL-D to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close() # Not strictly necessary here
# in_file.close()
