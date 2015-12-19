from string import ascii_lowercase

def encode(words):
    no_punc = ''.join([char.lower() for char in words if char.isalnum()])
    translated = ''
    for char in no_punc:
        if char in ascii_lowercase:
            i = ascii_lowercase.index(char)
            translated += ascii_lowercase[25 - i]
        else:
            translated += char
    return ' '.join([translated[i:i+5] for i in range(0, len(translated), 5)])

def decode(words):
    result = ''
    for char in words:
        if not char.isspace():
            if char in ascii_lowercase:
                i = ascii_lowercase.index(char)
                result += ascii_lowercase[25 - i]
            else:
                result += char
    return result
