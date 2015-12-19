from string import ascii_lowercase
from itertools import cycle
import random

class Cipher:
    def __init__(self, key=''):
        self.key = key
        if not self.key:
            length = random.randint(100, 200)
            for i in xrange(length):
                self.key += random.choice(ascii_lowercase)
        if not (self.key.isalpha() and self.key.islower()):
            raise ValueError("Key must contain only lowercase letters.")
   
    def encode(self, words):
        cycle_keys = cycle(self.key)
        result = ''
        for char in words:
            current_key = cycle_keys.next()
            shift = ascii_lowercase.index(current_key)
    	    if char.isalpha():
    	        i = (ascii_lowercase.index(char.lower()) + shift) % 26
    	        result += ascii_lowercase[i]
        return result

    def decode(self, words):
        cycle_keys = cycle(self.key)
        result = ''
        for char in words:
            current_key = cycle_keys.next()
            shift = ascii_lowercase.index(current_key)
            i = (ascii_lowercase.index(char.lower()) - shift) % 26
            result += ascii_lowercase[i]
        return result

class Caesar(Cipher):
    def __init__(self):
	    Cipher.__init__(self, 'd')