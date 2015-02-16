from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like this %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# Notice the implicit newline below
print """
Alright, so you said %r about liking this.
You live in %r. Not sure what that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
# ... and above.
