#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.random_numbers import generate_random_numbers
from brain_games.check_answers_if_even import get_answers
from brain_games.actions_depending_on_users_answer import *

def find_correct_answer(number):
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer

def main():
    n = 0
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while 0 <= n < 3:
        number = generate_random_numbers()
        print('Question:', number)
        user_answer = get_answers()
        correct_answer = find_correct_answer(number)
        if check(user_answer, correct_answer):
            n = do_if_correct(n)
        else:
            do_if_wrong(user_answer, correct_answer, name)
            break
        do_if_three_in_row(n, name)



if __name__ == '__main__':
    main()
