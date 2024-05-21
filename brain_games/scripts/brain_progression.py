#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.random_numbers import generate_random_numbers
from brain_games.get_users_answer import get_answers
from brain_games.actions_depending_on_users_answer import *


def generate_progression(start_number, step_number):
    progression = [start_number]
    a = start_number
    for i in range(10):
        a += step_number
        progression.append(a)
    return progression


def ask_question(progression, position):
    correct_answer = progression[position]
    progression[position] = '..'
    pr = ''
    for val in progression:
        pr = str(pr) + str(val) + ' '
    print(f'Question: {pr}')
    return correct_answer


def main():
    n = 0
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')
    while 0 <= n < 3:
        start_number = generate_random_numbers()
        step_number = generate_random_numbers(10)
        progression = generate_progression(start_number, step_number)
        position = generate_random_numbers(10)
        correct_answer = ask_question(progression, position)
        user_answer = get_answers()
        if check(user_answer, correct_answer):
            n = do_if_correct(n)
        else:
            do_if_wrong(user_answer, correct_answer, name)
            break
        do_if_three_in_row(n, name)


if __name__ == '__main__':
    main()
