#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.random_numbers import generate_random_numbers
from brain_games.get_users_answer import get_answers
from brain_games.actions_depending_on_users_answer import *
from random import choice


def generate_operator():
    """Generates random operation"""
    operator = choice('+-*')
    return operator


def question(number1, number2, operator):
    question = str(number1) + ' ' + str(operator) + ' ' + str(number2)
    print(f'Question: {question}')
    if operator == '+':
        correct_answer = number1 + number2
    elif operator == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    return correct_answer


def main():
    n = 0
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    while 0 <= n < 3:
        number1 = generate_random_numbers()
        number2 = generate_random_numbers()
        operator = generate_operator()
        correct_answer = question(number1, number2, operator)
        user_answer = get_answers()
        if check(user_answer, correct_answer):
            n = do_if_correct(n)
        else:
            do_if_wrong(user_answer, correct_answer, name)
            break
        do_if_three_in_row(n, name)


if __name__ == '__main__':
    main()
