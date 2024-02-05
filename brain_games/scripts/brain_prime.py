#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.random_numbers import generate_random_numbers
from brain_games.check_answers_if_even import get_answers
from brain_games.compare_prime import compare_answers
from brain_games.keep_the_score_prime import score_keeper
#from brain_games.cli import name


def main():
	n = 0
	print('Welcome to the Brain Games!')
	name = welcome_user()
	print('Answer "yes" if the number is even, otherwise answer "no".')
	number = generate_random_numbers()
	print ('Question:', number)
	user_answer = get_answers()
	n = compare_answers(number, user_answer, name, n)
	'''print (a)'''
	#got n - number of correct answers in a row
	score = score_keeper(n, name)


if __name__ == '__main__':
	main()