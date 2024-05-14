#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.random_numbers import generate_random_numbers
from brain_games.question_gcd import print_question
from brain_games.find_gcd import find_gcd
from brain_games.check_answers_if_even import get_answers
from brain_games.check import check_answers
from brain_games.counter_gcd import counter

def main():
    n = 0
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    number1 = generate_random_numbers()
    number2 = generate_random_numbers()
    print_question (number1, number2)
    correct_answer = find_gcd(number1, number2)
    user_answer = get_answers()
    n = check_answers(n, name, correct_answer, user_answer)
    #got n - number of correct answers in a row
    counter(n, name)


if __name__ == '__main__':
    main()