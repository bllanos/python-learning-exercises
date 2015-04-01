length = 10
ten_things = "Apples Oranges Crows Telephone Light Sugar"
stuff = ten_things.split(' ')

print "There are %d things in the list, which is not %d? (%s)" % (len(stuff), length, len(stuff) != length)
if len(stuff) != length:
    print "Let's fix that."

    more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "It"]

    while len(stuff) != 10:
        next_one = more_stuff.pop()
        print "Adding: ", next_one
        stuff.append(next_one)
        print "There are %d items now." % len(stuff)

    print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # Last element
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5]) # Slice
