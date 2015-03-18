# Lists can store values of mixed types
mixedList = ['a', 1, True]
print mixedList

# Multi-line lists
multiLineList = [
    'a',
    'b',
    'c', 'd'
    ]
print multiLineList

# List within a list
doubleList = [range(1,10), 'end']
print doubleList

# Operator overloading?
doubleList += '1' # It works.
print doubleList
