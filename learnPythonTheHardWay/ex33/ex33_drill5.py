def makeNumbers(n, inc):
    numbers = []
    i = 0
    for i in range(0, n, inc):
        print "At the top i is %d" % i
        numbers.append(i)
        # i += 3 This has no effect because `i` is re-initialized every iteration
        print "Numbers now:", numbers
    return numbers

print "The numbers: "

for num in makeNumbers(8, 2):
    print num
