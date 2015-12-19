arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

def numeral(number):
	result = ""
	for i in range(len(arabic)):
		while number >= arabic[i]:
			result += roman[i]
			number -= arabic[i]
	return result