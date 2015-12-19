hex_to_dec = {
              '0': 0,
              '1': 1,
              '2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9,
              'a': 10,
              'b': 11,
              'c': 12,
              'd': 13,
              'e': 14,
              'f': 15
              }

def hexa(num):
    hex = num.lower()
    if any(digit not in hex_to_dec for digit in hex):
        raise ValueError('Not a hexadecimal number.')
    dec = 0
    for i in range(len(hex)):
        dec += hex_to_dec[hex[i]] * 16 ** (len(hex) - i - 1)
    return dec