days = {
        1:  ['first', 'a Partridge in a Pear Tree.\n'],
        2:  ['second', 'two Turtle Doves, and '],
        3:  ['third', 'three French Hens, '],
        4:  ['fourth', 'four Calling Birds, '],
        5:  ['fifth', 'five Gold Rings, '],
        6:  ['sixth', 'six Geese-a-Laying, '],
        7:  ['seventh', 'seven Swans-a-Swimming, '],
        8:  ['eighth', 'eight Maids-a-Milking, '],
        9:  ['ninth', 'nine Ladies Dancing, '],
        10: ['tenth', 'ten Lords-a-Leaping, '],
        11: ['eleventh', 'eleven Pipers Piping, '],
        12: ['twelfth', 'twelve Drummers Drumming, ']
        }

def verse(n):
    result = "On the %s day of Christmas my true love gave to me, " % days[n][0]
    for i in range(n, 0, -1):
        result += days[i][1]
    return result

def verses(start, stop):
    return "\n".join([verse(i) for i in range(start, stop + 1)]) + "\n"

def sing():
    return verses(1, 12)