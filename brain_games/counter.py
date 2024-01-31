from check_answers_if_even import get_answers
from random_numbers import generate_random_numbers
from compare import compare_answers


def counter(n):
	while n < 3:
		number1 = generate_random_numbers()
		number2 = generate_random_numbers()
		operator = generate_operator()
		correct_answer = question (number1, number2, operator)
		user_answer = get_answers()
		n = check_answers(n, name, correct_answer, user_answer)
	print(f'Congratulations, {name}!')
	return (n)