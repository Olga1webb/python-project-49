from brain_games.check_answers_if_even import get_answers
from brain_games.random_numbers import generate_random_numbers
from brain_games.compare import compare_answers

def score_keeper(n, name):
    while 0 < n < 3:
        number = generate_random_numbers()
        print ('Question:', number)
        user_answer = get_answers()
        n = compare_answers(number, user_answer, name, n)
        if n == 3:
            print(f'Congratulations, {name}!')
    return (n)