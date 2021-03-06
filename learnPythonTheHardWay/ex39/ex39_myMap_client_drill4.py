import ex39_myMap as hashmap

# Create a mapping of state to abbreviations
states = hashmap.new()
stateNames = ['Oregon', 'Florida', 'California', 'New York', 'Michigan']
stateAbbreviations = ['OR', 'FL', 'CA', 'NY', 'MI']
for i, name in enumerate(stateNames):
    hashmap.set(states, name, stateAbbreviations[i])

# Create a basic set of states, and some cities in them
cityNames = ['Portland', 'Jacksonville', 'San Francisco', 'New York', 'Detroit']
cities = hashmap.new()
for i, name in enumerate(cityNames):
    hashmap.set(cities, stateAbbreviations[i], name)

# Print out some cities
def separator(n=10):
    print '-' * n

separator()
for i in [3, 0]:
    print "%s state has: %s" % (stateAbbreviations[i], hashmap.get(cities, stateAbbreviations[i]))
    assert hashmap.get(cities, stateAbbreviations[i]) == cityNames[i], \
        "Found incorrect city name in state to city mapping."

# Print some states
separator()
for i in [4, 1]:
    print "%s's abbreviation is: %s" % (stateNames[i], hashmap.get(states, stateNames[i]))
    assert hashmap.get(states, stateNames[i]) == stateAbbreviations[i], \
        "Found incorrect state abbreviation in state to state abbreviation mapping."

# do it by using the state then cities dict
separator()
for i in [4, 1]:
    print "%s has: %s" % (stateNames[i], hashmap.get(cities, hashmap.get(states, stateNames[i])))
    assert hashmap.get(cities, hashmap.get(states, stateNames[i])) == cityNames[i], \
        "Found incorrect city name using both mappings."

# Print every state abbreviation
separator()
hashmap.list(states)

# Print every city in state
separator()
hashmap.list(cities)

separator()
state = hashmap.get(states, 'Texas')

assert state == None
if not state:
    print "Sorry, no Texas."

city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
assert city == 'Does Not Exist'
