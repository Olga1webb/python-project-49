#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.random_numbers import generate_random_numbers
from brain_games.check_answers_if_even import get_answers
from brain_games.compare import compare_answers
#from brain_games.cli import name


def main():
	print('Welcome to the Brain Games!')
	name = welcome_user()
	print('Answer "yes" if the number is even, otherwise answer "no".')
	number = generate_random_numbers()
	user_answer = get_answers()
	a = compare_answers(number, user_answer, name)
	'''print (a)'''

if __name__ == '__main__':
	main()