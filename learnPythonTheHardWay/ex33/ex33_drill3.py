def makeNumbers(n, inc):
    numbers = []
    i = 0
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i += inc
        print "Numbers now:", numbers
        print "At the bottom, i is %d" % i
    return numbers

print "The numbers: "

for num in makeNumbers(8, 2):
    print num
