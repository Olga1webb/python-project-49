#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.random_numbers import generate_random_numbers
from brain_games.get_users_answer import get_answers
from brain_games.actions_depending_on_users_answer import *
import math


def print_question(number1, number2):
    print(f'Question: {number1} {number2}')


def find_gcd(number1, number2):
    correct_answer = math.gcd(number1, number2)
    return correct_answer


def main():
    n = 0
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    while 0 <= n < 3:
        number1 = generate_random_numbers()
        number2 = generate_random_numbers()
        print_question(number1, number2)
        correct_answer = find_gcd(number1, number2)
        user_answer = get_answers()
        if check(user_answer, correct_answer):
            n = do_if_correct(n)
        else:
            do_if_wrong(user_answer, correct_answer, name)
            break
        do_if_three_in_row(n, name)


if __name__ == '__main__':
    main()
