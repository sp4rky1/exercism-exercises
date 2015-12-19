from fractions import gcd

def primitive_triplets(b):
    if b % 4 != 0:
        raise ValueError('Argument must be divisible by 4')
    half = b / 2
    i = 1
    j = half
    result = []
    while i <= half ** 0.5:
        if j % 1 == 0 and gcd(i, j) == 1:
            a = j ** 2 - i ** 2
            c = j ** 2 + i ** 2
            triple = (a, b, c)
            result.append(tuple(sorted(triple)))
        i += 1
        while half % i != 0:
            i += 1
        j = half / i
    return set(result)

def triplets_in_range(min, max):
    result = []
    div_by_four = [n for n in range(max + 1) if n % 4 == 0]
    for num in div_by_four:
        primitives = primitive_triplets(num)
        for primitive in primitives:
            triplet = list(primitive)
            while all(n <= max for n in triplet):
                if all(min <= n for n in triplet):
                    result.append(tuple(triplet))
                for i in range(3):
                    triplet[i] += primitive[i]
    return set(result)

def is_triplet(triplet):
    abc = sorted(triplet)
    return abc[0] ** 2 + abc[1] ** 2 == abc[2] ** 2