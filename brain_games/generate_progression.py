from brain_games.random_numbers import generate_random_numbers


def generate_progression(start_number, step_number):
    progression = [start_number]
    a = start_number
    for i in range(10):
        a += step_number
        progression.append(a)
    return progression
