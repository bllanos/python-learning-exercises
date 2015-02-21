def inputAndPrint(*args):
    for val in args:
        print "You entered %r" % raw_input("%s: " % val)

inputAndPrint("Prompt 1", "Prompt 2")
