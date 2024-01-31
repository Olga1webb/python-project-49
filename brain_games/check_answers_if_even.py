def get_answers():
	"""Get user answer and the correct answer"""

	
	answer = input('Your answer: ')
	return answer

'''def compare_answers():
	"""Compare user answer and the correct answer"""
	correct_answer = bool(random_number // 2 == 0)
	number_of_correct_answers = 0

	if (answer == 'yes' and correct_answer == False) or (answer == 'no' and correct_answer == True):
		number_of_correct_answers += 1
		print('Correct!')

		if number_of_correct_answers == 3:
			print(f'Congratulations, {name}!')
			number_of_correct_answers = 0

	else:
		number_of_correct_answers = 0
		print(answer, ' is wrong answer ;(. Correct answer was \'no\'.')
		print(f'Let\'s try again, {name}!')'''
