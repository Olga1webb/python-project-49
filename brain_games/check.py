from brain_games.check_answers_if_even import get_answers
from brain_games.question import question
from brain_games.cli import welcome_user

def check_answers(n, name, correct_answer, user_answer):
    if str(user_answer) == str(correct_answer):
        a = 'Correct!'
        n += 1
        print(a)
        return(n)
    else:
        n = 0
        a =    f"'{user_answer}'' is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}!"
        print(a)
        return(n)