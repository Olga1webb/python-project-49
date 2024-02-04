#from random_numbers import generate_random_numbers

def ask_question(progression, position):
	correct_answer = progression[position]
	progression[position] = '..'
	pr = ''
	for val in progression:
		pr = str(pr) + str(val) + ' '
	print(f'Question: {pr}')
	return correct_answer
