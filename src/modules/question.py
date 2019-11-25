'''
This module deals with finding out the properties of the question such as:
1) what type of answer does a question expects.
'''

import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


class AnswerType():

	def __init__(self, question):
		# self.drop_len = 1
		self.tokens = self.cleanse(question)
		self.a_type = self.generate_answer_type()

	'''
	Remove punctuations and convert to lower form.
	'''
	def cleanse(self, question):
		temp = word_tokenize(question)
		output = []
		for token in temp:
			if not token in string.punctuation:
				output.append(token.lower())
		return output


	def generate_answer_type(self):
		return ["OPEN"]
		if self.tokens[0] == "who" or self.tokens[0] == "whom":
				return ["PERSON", "ORGANIZATION"]
			
		elif self.tokens[0] == "where":
			return ["LOCATION"]
			
		elif self.tokens[0] == "when":
			return ["DATE"]
			
		elif self.tokens[0] == "how":
				
			quantity = ["many", "much", "often"]
			linear_measure = ["long", "tall", "wide", "high", "big", "far"]		
				
			if self.tokens[1] in quantity:
				# self.drop_len = 2
				return ["QUANTITY", "TIME"]

			elif self.tokens[1] in linear_measure:
				# self.drop_len = 2
				return ["LINEAR_MEASURE"]

			else:
				return

		elif self.tokens[0] == "what" or self.tokens[0] == "which":
			if "name" in self.tokens:
				return ["PERSON"]
			elif "city" in self.tokens:
				return ["LOCATION"]
			elif "country" in self.tokens:
				return ["LOCATION"]
			elif "year" in self.tokens:
				return ["DATE"]
			elif "organization" in self.tokens:
				return ["ORGANIZATION"]
			elif "company" in self.tokens:
				return ["ORGANIZATION"]
			elif "total" in self.tokens:
				return ["QUANTITY"]
			elif "percentage" in self.tokens:
				return ["QUANTITY"]
			else:
				return ["OPEN"]
		else:
			return []

if __name__ == "__main__":
	question = input()
	# at = AnswerType("Who is the prime minister of India?")
	at = AnswerType(question)
	print(at.a_type)