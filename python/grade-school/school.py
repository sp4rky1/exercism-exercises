class School:
	def __init__(self, name):
		self.name = name
		self.db = {}
		
	def add(self, student, grade):
		if grade in self.db:
			self.db[grade] = self.db[grade] | {student}
		else:
			self.db[grade] = {student}
	
	def grade(self, n):
		if n in self.db:
			return self.db[n]
		return set()
	
	def sort(self):
		result = []
		for grade, students in sorted(self.db.items()):
			result.append((grade, tuple(sorted(students))))
		return result
	