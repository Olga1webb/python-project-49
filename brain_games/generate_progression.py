from random_numbers import generate_random_numbers


def generate_progression(start_number, step_number):
	progression = [start_number]
	
	for a in range(10):
		i = start_number + step_number
		progression.append(i)
		a += 1
	return progression

