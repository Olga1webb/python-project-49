def check(user_answer, correct_answer):
	return str(user_answer) == str(correct_answer)


def do_if_correct(n):
    print('Correct!')
    n += 1
    return n


def do_if_wrong(user_answer, correct_answer, name):
	print(f"'{user_answer}' is wrong answer ;(.\
	Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
	n = 0


def do_if_three_in_row(n, name):
    if n == 3:
        print(f'Congratulations, {name}!')
