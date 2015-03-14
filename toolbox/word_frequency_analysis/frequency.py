""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """
import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	punctuation = string.punctuation
	word_list = []
	with open(file_name, "r") as list_of_words:
	    words = list_of_words.read().split(' ')
	    for j in words:
	    	word = ''
	    	for i in j:
	    		if i not in punctuation and i not in ['\n','\r\n']:
	    			word+=i
	    	word.replace(' ', "")
	    	word_list.append(word.lower())
	return get_top_n_words(word_list,100)

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_count = {}
	for word in word_list:
		word_count[word] = word_count.get(word,0)+1
	#breaks dictionary into lists of values and keys
	v=word_count.values()
	k=word_count.keys()
	new_dict = {}
	#loops through to find inputted number of frequent words
	if len(word_count) < n:
		num = len(word_count)
	for i in range(0,n):
		key = k[v.index(max(v))]
		val = max(v)
		new_dict[key] = val
		#removes the word from word_count to find next highest word count
		k.remove(key)
		v.remove(val)
	new_dict = sorted(new_dict.items(), key=lambda item: item[1],reverse=True)
	return [i[0] for i in new_dict]

print get_word_list('TheLittlePrince.txt')