class Garden:
	default_students = "Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()
	def __init__(self, diagram, students=default_students):
		self.diagram = diagram.split()
		number_of_students = len(self.diagram[0])
		self.students = sorted(students)[:number_of_students]
		
	def plants(self, student):
		plants_dic = {"G": "Grass",
					  "C": "Clover",
					  "R": "Radishes",
					  "V": "Violets"}
		i = self.students.index(student)
		plant_letters = self.diagram[0][2*i:2*i+2] + self.diagram[1][2*i:2*i+2]
		result = []
		for char in plant_letters:
			result.append(plants_dic[char])
		return result