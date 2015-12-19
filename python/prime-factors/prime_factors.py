def prime_factors(number):
	divisor = 2
	result = []
	while number > 1:
		while number % divisor == 0:
			result.append(divisor)
			number /= divisor
		divisor += 1
	return result