from check_answers_if_even import get_answers
from question import question
from cli import welcome_user

def check_answers(n, name, correct_answer, user_answer):
	if correct_answer == user_answer:
		a = 'Correct!'
		n += 1
	else:
		a =	"f'{user_answer} is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}"
	print(a)
	return(n)