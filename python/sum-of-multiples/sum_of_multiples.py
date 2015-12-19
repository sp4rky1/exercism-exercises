def sum_of_multiples(n, factors=[3, 5]):
	multiples = set()
	for factor in factors:
		if factor > 0:
			multiples = multiples | set(xrange(factor, n, factor))
	return sum(multiples)