class Allergies:
    def __init__(self, score):
        self.score = score
        self.lst = self.all_allergies()

    def all_allergies(self):
        allergy_scores = {1:   'eggs',
                          2:   'peanuts',
                          4:   'shellfish',
                          8:   'strawberries',
                          16:  'tomatoes',
                          32:  'chocolate',
                          64:  'pollen',
                          128: 'cats'}
        remainder = self.score
        result = []
        for num, allergy in sorted(allergy_scores.items(), reverse=True):
            if remainder >= num:
                remainder -= num
                result.append(allergy)
        return result
    
    def is_allergic_to(self, food):
        return food in self.lst
