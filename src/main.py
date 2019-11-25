from modules.answer import Extract
from modules.document import PassageRetrieval 
from modules.question import AnswerType
from modules.sentence import SentenceRetrieval

import numpy as np

abs_path = '/Users/lashitjain/Projects/FactoidQA/dataset/curated/'
print("Absolute Path: " +  abs_path + ". If you're using different platform, alter it in main.py")
file_name = input("Enter name: ")
doc_path = abs_path + file_name + '/document.txt'
qst_path = abs_path + file_name + '/question.txt'
ans_path = abs_path + file_name + '/answer.txt'

questions = open(qst_path).readlines()
answers = open(ans_path).readlines()
ans_indx = 0
correct = 0

for question in questions:
	pr = PassageRetrieval(doc_path, question)
	passage = pr.passages[np.argmax(pr.ranking)]

	sr = SentenceRetrieval(passage, question)
	indices = np.array(sr.rank).argsort()[-len(sr.rank):][::-1]
	print(question.strip())
	for index in indices:
		sentence = sr.base[index]
		# print(sentence)
		ex = Extract(sentence, AnswerType(question).a_type, question)
		if not ex.answer:
			continue
		# if ex.answer in answers[ans_indx].split('*'):
		# 	correct += 1
		# Since answers provided by the SQuAD are not very clean
		for answer in answers[ans_indx].split('*'):
			if answer:
				if ex.answer in answer:
					correct += 1
					break
				elif answer in ex.answer:
					correct += 1
					break
		print(ex.answer)
		break
	print()
	ans_indx+=1

print(str((correct/len(questions)) * 100) + '%')



