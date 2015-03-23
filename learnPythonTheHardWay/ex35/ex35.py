from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice: # Treating a string as a sequence of characters
        how_much = int(choice)
    else:
        dead("Type a number.")

    if how_much < 50:
        print "Nice, you're not greedy. You win!"
        exit(0)
    else:
        dead("A bit too much.")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear kills you.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear didn't like it.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "Cannot process that action."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "It stares at you and you go insane."
    print "Do you flee for your life?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("What did you expect?")
    else:
        cthulhu_room()

def dead(why):
    print why, "So long."
    exit(0)

def start():
    print "You are in a dark room."
    print "There are doors to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left": # 'is' tests for identity, not value equality! Use '==' instead.
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You didn't go anywhere.")

start()
