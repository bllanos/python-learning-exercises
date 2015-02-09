my_name = 'bllanos'
my_age = 35 # not really
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print 'Can I put format strings in single-quote delimited strings, %s?' % my_name # Yes
# More on this at
# [Stack Overflow](http://stackoverflow.com/questions/628657/difference-between-the-use-of-double-quote-and-quotes-in-python#628750)
print "They are %d inches tall." % my_height
print "They are %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "They've got %s eyes and %s hair." % (my_eyes, my_hair)
print "Their teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d and %d, I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
