def counter(n):
	while n < 3:
		number1 = generate_random_numbers()
		number2 = generate_random_numbers()
		operator = generate_operation()
		correct_answer = question (number1, number2, operator)
		user_answer = get_answers()
		n = check_answers(n, name, correct_answer, user_answer)
	print(f'Congratulations, {name}!')
	return (n)