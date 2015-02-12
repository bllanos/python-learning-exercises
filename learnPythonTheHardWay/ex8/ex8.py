formatter = "%r %r %r %r"

print formatter # Proves that the formatting operators do nothing unless the string is followed by '%'
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.", # Because this contains `'`, repr() surrounds the
    # output with double quotes instead of the usual single quotes.
    "So I said goodnight."
)

print formatter % (
    formatter % (1, 2, 3, 4),
    formatter % (1, 2, 3, 4),
    formatter % (1, 2, 3, 4),
    formatter % (1, 2, 3, 4)
)

print "Test %s" % "can't" # Obviously, `'` makes no difference here.
