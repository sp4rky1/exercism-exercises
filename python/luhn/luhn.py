class Luhn:
	def __init__(self, number):
		self.number = number
	
	def addends(self):
		reversed_list = [int(n) for n in str(self.number)[::-1]]
		for i in range(1, len(reversed_list), 2):
			x = 2 * reversed_list[i]
			if x >= 10:
				reversed_list[i] = x - 9
			else:
				reversed_list[i] = x
		return list(reversed(reversed_list))
	
	def checksum(self):
		return sum(self.addends()) % 10
	
	def is_valid(self):
		return self.checksum() == 0
	
	@staticmethod
	def create(n):
		return 10 * n + (10 - Luhn(10 * n).checksum()) % 10