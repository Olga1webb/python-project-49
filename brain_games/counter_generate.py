from check_answers_if_even import get_answers
from random_numbers import generate_random_numbers
from random_numbers_to_ten import generate_random_numbers_to_ten
from generate_progression import generate_progression
from ask_question import ask_question
from check import check_answers


def counter(n, name):
	while 0 < n < 3:
		start_number = generate_random_numbers()
		step_number = generate_random_numbers_to_ten()
		progression = generate_progression(start_number, step_number)
		position = generate_random_numbers_to_ten()
		correct_answer = ask_question(progression, position)
		user_answer = get_answers()
		n = check_answers(n, name, correct_answer, user_answer)
		if n == 3:
			print(f'Congratulations, {name}!')
	return (n)