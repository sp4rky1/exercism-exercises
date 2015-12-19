from itertools import product

def smallest_palindrome(max_factor, min_factor=0):
    value = int
    factors = set()
    products = product(xrange(min_factor, max_factor + 1), repeat=2)
    pair = products.next()
    while True:
        x = pair[0] * pair[1]
        if x < value and str(x) == str(x)[::-1]:
            value = x
            factors = set(pair)
        try:
            pair = products.next()
        except StopIteration:
            break
    return (value, factors)
    
def largest_palindrome(max_factor, min_factor=0):
    value = 0
    factors = set()
    products = product(xrange(max_factor, min_factor - 1, -1), repeat=2)
    pair = products.next()
    while True:
        x = pair[0] * pair[1]
        if x > value and str(x) == str(x)[::-1]:
            value = x
            factors = set(pair)
        try: 
            pair = products.next()
        except StopIteration:
            break
    return (value, factors)