people = 20
cats = 30
dogs = 15

if people < cats: # True
    print "Too many cats! The world is doomed!"

if people > cats: # False
    print "Not many cats! The world is doomed!"
    
if people < dogs: # False
    print "The world is drooled on!"

if people > dogs: # True
    print "The world is dry!"
    
dogs += 5

if people >= dogs: # True
    print "People are greater than or equal to dogs."
    
if people <= dogs: # True
    print "People are less than or equal to dogs."
    
if people == dogs: # True
    print "People are equivalent to dogs."
    
if not people != dogs: print "Single-line if-statement"

# Syntax error:
# if True:
# print "Syntax error?"
