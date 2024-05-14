from brain_games.check_answers_if_even import get_answers
from brain_games.random_numbers import generate_random_numbers
from brain_games.cli import welcome_user

def compare_answers(number, user_answer, name, n):
	'''user_answer = get_answers()
	number = generate_random_numbers()'''
	#name = welcome_user()
	for i in range(2,number):
		correct_answer = bool(number % i == 0)

	if (correct_answer is True and user_answer == 'yes') or (correct_answer is False and user_answer == 'no'):
		a ='Correct!'
		n +=1
		print(a)
		return(n)	

	else:
		n = 0
		if correct_answer is True:
			a = user_answer + " is wrong answer ;(. Correct answer was 'yes'\nLet's try again, " + name
		else:
			a = user_answer + " is wrong answer ;(. Correct answer was 'no'\nLet's try again, " + name
		print(a)	
		return(n)