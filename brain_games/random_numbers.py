from random import randint


def generate_random_numbers():
	"""Generates random numbers from 0 to 100"""
	random_number = randint(0,100)
	print ('Question:', random_number)
	return random_number
