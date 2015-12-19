def transform(old):
	new = {}
	for key in old:
		for char in old[key]:
			new[char.lower()] = key
	return new
	