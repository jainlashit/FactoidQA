from nltk import ngrams
from nltk.tokenize import sent_tokenize

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vector import BuildVector


class SentenceRetrieval:
	def __init__(self, passage, question, ngram=2):
		self.base = []
		self.s_token = []
		for sentence in sent_tokenize(passage):
			self.base.append(sentence)
			self.s_token.append([*BuildVector(sentence).value])
		self.q_token = [*BuildVector(question).value]
		self.rank = [0] * len(self.base)
		for n in range(1, ngram+1):
			self.similarity(n)



	# similarity is computed on the basis of ngrams
	def similarity(self, ngram):
		s_gram = []
		for token in self.s_token:
			s_gram.append(set(ngrams(token, ngram)))
		q_gram = set(ngrams(self.q_token, ngram))
		for index in range(len(self.base)):
			# higher weight to higher ngrams
			self.rank[index] += ngram * len(s_gram[index]&q_gram)

if __name__ == "__main__":
	passage = 'In 1906, precipitation hardening alloys were discovered by Alfred Wilm. Alloys are formed from metals.'
	question = 'Who discovered precipitation hardening alloy'
	sr = SentenceRetrieval(passage, question)
	print(sr.rank)
