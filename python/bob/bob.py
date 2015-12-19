def hey(what):
    x = what.rstrip()
    if what.isupper():
        return 'Whoa, chill out!'
    elif len(x) == 0:
        return 'Fine. Be that way!'
    elif x.endswith('?'):
        return 'Sure.'
    return 'Whatever.'
