class Matrix:
    def __init__(self, values):
        self.rows = []
        for row in values.split('\n'):
            self.rows.append([int(n) for n in row.split()])
        
        self.columns = []
        for i in range(len(self.rows[0])):
            self.columns.append([self.rows[j][i] for j in range(len(self.rows))])