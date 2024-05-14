from brain_games.operations import generate_operator
from brain_games.random_numbers import generate_random_numbers

def question(number1, number2, operator):
	question = str(number1) + str(operator) + str(number2)
	print(f'Question: {question}')
	if operator == '+':
		correct_answer = number1 + number2
	elif operator == '-':
		correct_answer = number1 - number2
	else:
		correct_answer = number1 * number2

	return correct_answer