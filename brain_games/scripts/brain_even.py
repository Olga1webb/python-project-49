def brain_even_game():
	number_of_correct_answers = 0
	number_of_tries = 0

	print('Answer "yes" if the number is even, otherwise answer "no".')

	from random import randint


	random_number = randint(0,100)
	correct_answer = bool(random_number // 2 == 0)
	answer = prompt.string('Question: ', random_number)
	
	print('Your answer: ', answer)

	if (answer == 'yes' and correct_answer == True) or (answer == 'no' and correct_answer == False):
		number_of_correct_answers += 1
		print('Correct!')

		if number_of_correct_answers == 3:
			return f'Congratulations, {name}!'
			number_of_correct_answers = 0
			
	else:
		number_of_correct_answers = 0
		print(answer, ' is wrong answer ;(. Correct answer was \'no\'.')
		return f'Let\'s try again, {name}!'
