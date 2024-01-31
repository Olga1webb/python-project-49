from check_answers_if_even import get_answers
from question import question
from cli import welcome_user

def check_answers(n, name, correct_answer, user_answer):
	if int(user_answer) == int(correct_answer):
		a = 'Correct!'
		n += 1
		print(a)
		return(n)
	else:
		n = 0
		a =	f"'{user_answer}'' is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}"
		print(a)
		return(n)