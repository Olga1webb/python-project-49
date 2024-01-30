from check_answers_if_even import get_answers
from random_numbers import generate_random_numbers

def compare_answers(number, user_answer):
	'''user_answer = get_answers()
	number = generate_random_numbers()'''
	correct_answer = bool(number % 2 == 0)
	if (correct_answer is True and user_answer == 'yes') or (correct_answer is False and user_answer == 'no'):
		a ='Correct!'

	else:
		a = 'Wrong!'
	print (a)	
	return (a)