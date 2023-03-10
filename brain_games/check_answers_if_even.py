import prompt
from brain_games.random_numbers import generate_random_numbers
from brain_games.cli import welcome_user



def answers():
	"""Get user answer and the correct answer"""
	generate_random_numbers()

	correct_answer = bool(random_number // 2 == 0)
	answer = prompt.string('Question: ', random_number)
	print('Your answer: ', answer)

	
def compare_answers():
	"""Compare user answer and the correct answer"""
	if (answer == 'yes' and correct_answer == True) or (answer == 'no' and correct_answer == False):
		number_of_correct_answers += 1
		print('Correct!')

		if number_of_correct_answers == 3:
			print(f'Congratulations, {name}!')
			number_of_correct_answers = 0
			
	else:
		number_of_correct_answers = 0
		print(answer, ' is wrong answer ;(. Correct answer was \'no\'.')
		print(f'Let\'s try again, {name}!')