import json
import os

base_path = '//Users/lashitjain/Projects/FactoidQA/dataset/curated/'

def main():
	with open("dev-v1.1.json") as json_file:
		dataset = json.load(json_file)

	for name in dataset['data']:
		print(name['title'])

	index = input("index>")
	document = dataset['data'][int(index)]

	dir_name = base_path + document['title']
	print(document['title'])
	command = input("Select(y/n)> ")
	if command != "y":
		return
	if not os.path.exists(dir_name):
	    os.makedirs(dir_name)

	os.remove(dir_name + "/document.txt")
	os.remove(dir_name + "/question.txt")
	os.remove(dir_name + "/answer.txt")

	doc_file = open(dir_name + "/document.txt", 'a')
	qst_file = open(dir_name + "/question.txt", 'a')
	ans_file = open(dir_name + "/answer.txt", 'a')

	paragraphs = document['paragraphs'][:25]
	count = 0
	max_count = 25

	for paragraph in paragraphs:
		qas = paragraph['qas']
		doc_file.write(paragraph['context'] + "\n")
		for qa in qas:
			
			print(qa['question'])
			
			answers = ''
			for answer in qa['answers']:
				print(answer['text'])
				answers += answer['text'] + '*'

			command = input("Select(y/n)> ")
			if command != "y":
				continue
			qst_file.write(qa['question'] + "\n")
			ans_file.write(answers + "\n")
			count += 1

			if count == max_count:
				break

		if count == max_count:
			break

if __name__ == '__main__':
	main()

