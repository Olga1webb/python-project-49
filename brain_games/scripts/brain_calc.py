#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.random_numbers import generate_random_numbers
from brain_games.operations import generate_operator
from brain_games.question import question
from brain_games.check_answers_if_even import get_answers
from brain_games.check import check_answers


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
        n = check_answers(n, name, correct_answer, user_answer)
    # got n - number of correct answers in a row
        if n == 0:
            break
    if n == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
