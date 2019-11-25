from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from vector import BuildVector



class Score:
	def __init__(self, question, sentence, key):
		self.qVec = BuildVector(question).keys
		self.leftVec = BuildVector(sentence.split(key)[0]).keys
		self.rightVec = BuildVector(sentence.split(key)[1]).keys
		
		if len(sentence.split(key)) > 2:
			self.value = 0
		self.value = self.compute()

	def compute(self):
		score = 0
		for index in range(len(self.leftVec)):
			if self.leftVec[index] in self.qVec:
				score += 1/(len(self.leftVec) - index)

		for index in range(len(self.rightVec)):
			if self.rightVec[index] in self.qVec:
				score += 1/(index+1)
		return score
