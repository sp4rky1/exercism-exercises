from string import ascii_uppercase, digits
import random

class Robot:
    names = []
    
    def generate_name(self):
        name = ''
        for i in range(2):
            name += random.choice(ascii_uppercase)
        for i in range(3):
            name += random.choice(digits)
        return name
            
    def __init__(self):
        name = self.generate_name()
        while name in Robot.names:
            name = self.generate_name()
        Robot.names.append(name)
        self.name = name
        
    def reset(self):
        self.__init__()