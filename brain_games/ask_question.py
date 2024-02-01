#from random_numbers import generate_random_numbers

def ask_question(progression, position):
	correct_answer = progression[position]
	progression[position] = '..'
	print(f'Question: {progression}')
	return correct_answer
