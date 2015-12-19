import math

def encode(words):
    normalised = ''.join(char.lower() for char in words if char.isalnum())
    length = len(normalised)
    width = int(math.ceil(math.sqrt(length)))
    columns = [normalised[i::width] for i in range(width)]
    return ' '.join(columns)