# Some things to be explained in future exercises

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
"""
# Each line is printed on a new line.

string = """
A
multi
line
string
"""

print "string = %r" % string
# repr(string) is '\nA\nmulti\nline\nstring\n'

string2 = '''
Another
multi
line
string '''
print string2
