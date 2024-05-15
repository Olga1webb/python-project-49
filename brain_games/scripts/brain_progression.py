#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.random_numbers import generate_random_numbers
from brain_games.random_numbers_to_ten import generate_random_numbers_to_ten
from brain_games.generate_progression import generate_progression
from brain_games.ask_question import ask_question
from brain_games.check_answers_if_even import get_answers
from brain_games.check import check_answers
from brain_games.counter_generate import counter


def main():
    n = 0
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')
    start_number = generate_random_numbers()
    step_number = generate_random_numbers_to_ten()
    progression = generate_progression(start_number, step_number)
    position = generate_random_numbers_to_ten()
    correct_answer = ask_question(progression, position)
    user_answer = get_answers()
    n = check_answers(n, name, correct_answer, user_answer)
    # got n - number of correct answers in a row
    counter(n, name)


if __name__ == '__main__':
    main()
