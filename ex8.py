# 'r' is used to convert any Python object using repr() to a string. gives you the "raw" data as they appear (with quotes)
formatter = "%r %r %r %r"

# "%r %r %r %r" % (1, 2, 3, 4)
print formatter % (1, 2, 3, 4)
# "%r %r %r %r" % ("one", "two", "three", "four")
print formatter % ("one", "two", "three", "four")
print "%s %s %s %s" % ("one", "two", "three", "four")
#print True False False True
print formatter % (True, False, False, True)
#print "%r %r %r %r" four times
print formatter % (formatter, formatter, formatter, formatter)
#print four strings
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)