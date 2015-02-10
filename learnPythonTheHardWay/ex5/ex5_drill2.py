my_name = 'bllanos'
my_age = 35 # not really
my_height = 74 # inches
my_height_cm = my_height * 2.540 # centimetres
my_weight = 180 # lbs
my_weight_kg = my_weight * 0.4536 # kilograms
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "They are %d inches tall, or %d centimetres." % (my_height, my_height_cm)
print "They are %d pounds heavy, or %f kilograms." % (my_weight, my_weight_kg)
print "Actually", # The comma suppresses a newline.
print "that's not too heavy."
print # print a newline only
print "They've got %s eyes and %s hair." % (my_eyes, my_hair)
print "Their teeth are usually %s \
depending on the coffee." % my_teeth
# Break statement accross multiple lines - doesn't work with inline comments

print >> None , "This is the other form of print, 'print chevron'"
print "If I add %d, %d and %d, I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
