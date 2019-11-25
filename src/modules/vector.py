
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


class BuildVector:
	def __init__(self, phrase, stemming=True):
		# this value can either be question or a passage or a sentence or a document?
		self.base = phrase
		self.value = self.vector(stemming)
	
	'''
	Following function does two things:
	i) Convert all words involved into lower form
	ii) remove punctuations
	'''
	def cleanse(self):
		''' 
		TODO: This tokenization fuction separates don't into do n't :/
		Don't think it would matter much for our purpose but still...
		'''
		temp = word_tokenize(self.base)
		output = []
		for token in temp:
			if not token in string.punctuation:
				output.append(token.lower())
		return output

	def gen_query(self, stemming):
		query = []
		tokens = self.cleanse()
		ps = PorterStemmer()
		for word in tokens:
			if not word in stopwords.words("english"):
				if stemming:
					query.append(ps.stem(word))
				else:
					query.append(word)
		return query


	def vector(self, stemming):
		self.keys = self.gen_query(stemming)
		vector = {}
		for word in self.keys:
			if not word in vector:
				vector[word] = 1
			else:
				vector[word] += 1
		return vector

if __name__ == "__main__":

	passage = '''Hello. This is Lashit Jain. I'm a student at IIIT Hyderabad. 

	I would like to earn decent amount of money and serve my family and friends. I would also like to serve my society.

	I don't think so I have enough needs of my own except a comfortable place to sleep. The ultimate peace for me would be to serve the loved ones well.

	'''
	
	bv = BuildVector(passage)
	print(bv.value)
