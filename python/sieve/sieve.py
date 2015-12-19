def sieve(num):
    primes = xrange(2, num + 1)
    i = 0
    while i < len(primes):
        p = primes[i]
        primes = filter(lambda x: x % p != 0 or x <= p, primes)
        i += 1
    return primes
