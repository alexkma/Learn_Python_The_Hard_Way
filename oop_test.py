import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
	 "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
	 "class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	 "class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	 "Set *** to an instance of class %%%.",
	"***.***(@@@)":
	 "From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	 "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
	
# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	# strip() removes \n
	WORDS.append(word.strip())
	
# snippet is the key; phrase is the value
def convert(snippet, phrase):
	# random.sample(population, k)
	# Return a k length list of unique elements chosen from the population sequence. Used for random sampling without replacement.
	# print WORDS
	
	class_names = [w.capitalize() for w in
					random.sample(WORDS, snippet.count("%%%"))]
	# print "class_names: ", class_names
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	# print snippet.count("@@@")
	# does not enter for loop is snippet does not count "@@@"
	# range(0, 0) or range(0, 1)
	for i in range(0, snippet.count("@@@")):
		# random.randint(a, b)
		# Return a random integer N such that a <= N <= b.
		param_count = random.randint(1,3)
		# ['attention', 'caption'] => ['attention, caption']
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		
	for sentence in snippet, phrase:
		# print "sentence: ", sentence
		
		# result = sentence
		# result = sentence[:]
		result = sentence[:]
		# print "result: ", result
		
		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
			
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
			
		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
		# print "results: ", results
		
	return results
	
	
# keep going until they hit CTRL-D
try:
	while True:
		# get the keys of PHRASES
		# ["***.*** = '***'", '*** = %%%()', 'class %%%(object):\n\tdef ***(self, @@@)', '***.***(@@@)', 'class %%%(object):\n\tdef __init__(self, ***)', 'class %%%(%%%):']
		snippets = PHRASES.keys()
		random.shuffle(snippets)
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
				
			print question
			
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"