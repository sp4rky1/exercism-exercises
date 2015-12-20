from string import ascii_lowercase
def is_pangram(sentence):
    x = sentence.lower()
    if any(x.count(letter) == 0 for letter in ascii_lowercase):
        return False
    return True