tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line. Not sure how that is persian."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
"\t* Cat food" # Comments don't work here.
"\t* Fishies" # No need to escape double quotes
'\t* Catnip\n\t* Grass'
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Unicode
print u"\u00E8"
print u"\xE8"

while True:
    for i in ["/", " -", "|", "\\", "|"]:
        print "%s\r" % i,
# The carriage return sends the cursor back to the start of the line.
