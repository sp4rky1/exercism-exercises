def slices(digits, length):
    if length == 0:
        raise ValueError('Cannot have a slice of length 0')
    if length < 0:
        raise ValueError('Cannot have a slice of negative length')
    if length > len(digits):
        raise ValueError('Cannot have a slice longer than the number of digits')
    result = []
    for i in range(len(digits) - length + 1):
        slice = digits[i:length+i]
        result.append([int(num) for num in slice])
    return result