from check_answers_if_even import get_answers
from random_numbers import generate_random_numbers
from question_gcd import print_question
from find_gcd import find_gcd
from check_answers_if_even import get_answers
from check import check_answers


def counter(n, name):
	while 0 < n < 3:
		number1 = generate_random_numbers()
		number2 = generate_random_numbers()
		print_question (number1, number2)
		correct_answer = find_gcd(number1, number2)
		user_answer = get_answers()
		n = check_answers(n, name, correct_answer, user_answer)
		if n == 3:
			print(f'Congratulations, {name}!')
	return (n)