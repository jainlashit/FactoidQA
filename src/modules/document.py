import math

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vector import BuildVector

'''
PassageRetrieval helps with selecting top passage from a document by using TF IPF 
(Term Frequency Inverse Passage Frequency)
'''


class PassageRetrieval:
	def __init__(self, document_file, question):
		self.base = open(document_file).read()
		self.passages = self.get_passages(document_file)
		self.qVec = BuildVector(question).value
		self.pVec = []
		for passage in self.passages:
			self.pVec.append(BuildVector(passage).value)
		self.build_passage_frequency()
		self.ranking = self.cosine_match()


	def get_passages(self, document_file):
		passages = []
		for passage in open(document_file).readlines():
			if(len(passage.strip()) > 0):
				passages.append(passage.strip())
		return passages

	def build_passage_frequency(self):
		self.dVec = {}
		for vec in self.pVec:
			for entry in vec:
				if entry in self.dVec:
					self.dVec[entry] += 1
				else:
					self.dVec[entry] = 1

	# build term frequency inverse passage frequency for each passage.
	def tf_ipf(self):
		for vec in self.pVec:
			for entry in vec:
				# vec[entry] *= math.log((len(self.passages) + 1)/ self.dVec[entry])
				vec[entry] = math.log(vec[entry]*((len(self.passages) + 1)/ self.dVec[entry]))
				# vec[entry] = math.log((len(self.passages) + 1)/ self.dVec[entry])

	''' after getting the tf_ipf, cosine match vector of passages with question vector
	and return passages ranked.
	'''
	def cosine_match(self):
		self.tf_ipf()
		score = [0] * len(self.passages)
		for index in range(len(self.passages)):
			base = 0
			for entry in self.pVec[index]:
				base += self.pVec[index][entry] * self.pVec[index][entry]
			for entry in self.qVec:
				if entry in self.pVec[index]:
					score[index] += (self.pVec[index][entry] * self.qVec[entry])/math.sqrt(base)
		return score

if __name__ == "__main__":
	pr = PassageRetrieval('../text.txt', "Who discovered precipitation hardening alloy?")
	# print(pr.ranking)
