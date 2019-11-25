import spacy


import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from score import Score

# maps our tags to spacy's tags
conversion_index = {
	"PERSON": ["PERSON", "OPEN"],
	"NORP": ["OPEN"],
	"FAC": ["OPEN"],
	"ORG": ["ORGANIZATION", "OPEN"],
	"GPE": ["LOCATION", "OPEN"],
	"LOC": ["LOCATION", "OPEN"],
	"PRODUCT": ["OPEN"],
	"EVENT": ["OPEN"],
	"WORK_OF_ART": ["OPEN"],
	"LAW": ["OPEN"],
	"LANGUAGE": ["OPEN"],
	"DATE": ["DATE", "OPEN"],
	"TIME": ["TIME", "OPEN"],
	"PERCENT": ["QUANTITY", "OPEN"],
	"MONEY": ["QUANTITY", "OPEN"],
	"QUANTITY": ["LINEAR_MEASURE", "QUANTITY", "OPEN"],
	"ORDINAL": ["OPEN"],
	"CARDINAL": ["LINEAR_MEASURE", "QUANTITY", "OPEN"]
}

class Extract:
	def __init__(self, sentence, answer_type, question):
		self.base = sentence
		self.question = question
		self.exp = answer_type
		self.answer = self.process()

	# If there are multiple name entity
	def resolve(self, potential_answers):
		# print(potential_answers)
		output = None
		max_val = 0
		for answer in potential_answers:
			s = Score(self.question, self.base, answer).value
			if answer in self.question:
				s = -1
			if s >= max_val:
				max_val = s
				output = answer
		return output



	# Finds out named entities
	def process(self):
		potential_answers = []
		processor = spacy.load('en')
		named_entities = processor(self.base)
		for entity in named_entities.ents:
			for exp in self.exp:
				if exp in conversion_index[entity.label_]:
					potential_answers.append(str(entity))
		if len(potential_answers) > 1:
			return self.resolve(potential_answers)
		elif len(potential_answers) == 1:
			return potential_answers[0]

if __name__ == "__main__":
	ex = Extract("Before Genghis Khan died, he assigned Ögedei Khan as his successor and split his empire into khanates among his sons and grandsons.", ["PERSON"], "Who did Genghis Khan assign as his successor?")
	print(ex.answer)


