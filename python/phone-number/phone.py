class Phone:
    def __init__(self, number):
        only_digits = ''.join([num for num in number if num.isdigit()])
        if len(only_digits) < 10 or len(only_digits) > 11:
            self.number = '0' * 10
        elif len(only_digits) == 10:
            self.number = only_digits
        elif only_digits[0] == '1':
            self.number = only_digits[1:]
        elif only_digits[0] != '1':
            self.number = '0' * 10
    
    def area_code(self):
        return self.number[0:3]
    
    def pretty(self):
        return "(%s) %s-%s" % (self.number[0:3], self.number[3:6], self.number[6:10])