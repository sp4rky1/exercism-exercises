def calculate(question):
    sentence = question.rstrip('?').split(' ')
    total = int(sentence[2])
    i = 3
    while i < len(sentence):
        if sentence[i] == 'plus':
            total += int(sentence[i + 1])
            i += 2
        elif sentence[i] == 'minus':
            total -= int(sentence[i + 1])
            i += 2
        elif sentence[i] == 'divided':
            total /= int(sentence[i + 2])
            i += 3
        elif sentence[i] == 'multiplied':
            total *= int(sentence[i + 2])
            i += 3
        else:
            raise ValueError("invalid operation")
    return total