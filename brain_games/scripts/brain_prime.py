#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.random_numbers import generate_random_numbers
from brain_games.get_users_answer import get_answers
from brain_games.actions_depending_on_users_answer import *


def find_correct_answer(number):
    correct_answer = 'yes'
    for i in range(2, number):
        if number % i == 0:
            correct_answer = 'no'
            break
    return correct_answer


def main():
    n = 0
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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
