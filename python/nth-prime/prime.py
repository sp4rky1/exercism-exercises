def nth_prime(n):
    count = 1
    number = 2
    while count < n:
        number += 1
        if is_prime(number):
            count += 1
    return number

def is_prime(number):
    divisor = 2
    while divisor <= number ** 0.5:
        if number % divisor == 0:
            return False
        divisor += 1
    return number != 1