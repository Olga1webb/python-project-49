from brain_games.random_numbers import generate_random_numbers
from brain_games.check_answers_if_even import answers 
from brain_games.check_answers_if_even import compare_answers 


def brain_even_game():
	number_of_correct_answers = 0
	number_of_tries = 0

	print('Answer "yes" if the number is even, otherwise answer "no".')

	generate_random_numbers()
	answers()
	compare_answers()


	
	
