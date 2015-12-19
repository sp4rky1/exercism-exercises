def parse_binary(num):
    if any(digit != '0' and digit != '1' for digit in num):
        raise ValueError('Input is not a binary number.')
    result = 0
    for i in range(len(num)):
        digit = int(num[i])
        result += digit * 2 ** (len(num) - i - 1)
    return result