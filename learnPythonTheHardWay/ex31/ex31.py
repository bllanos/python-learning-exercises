print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

def prompt_for_number():
    while True:
        try:
            string = raw_input("> ")
            return int(string)
        except ValueError as err:
            print "Please enter an integer."

door = prompt_for_number()

if door == 1:
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Something sensible"
    
    bear = prompt_for_number()
    
    if bear == 1:
        print "The bear eats your face off. Good job!"
    elif bear == 2:
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == 2:
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Hyacinth in bloom."
    
    insanity = prompt_for_number()
    
    if insanity == 1 or insanity == 2:
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity is only temporary. Good job!"
        
else:
    print "You stumble around and find another door. Good job!"
