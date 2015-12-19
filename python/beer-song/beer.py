def verse(num):
    if num == 0:
        return "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"
    if num in xrange(3, 100):
        current = "%s bottles" % (num)
        one = "one"
        bottles_left = "%s bottles" % (num-1)
    elif num == 2:
        current = "2 bottles"
        one = "one"
        bottles_left = "1 bottle"
    elif num == 1:
        current = "1 bottle"
        one = "it"
        bottles_left = "no more bottles"
    result = "%s of beer on the wall, %s of beer.\nTake %s down and pass it around, %s of beer on the wall.\n" % (current, current, one, bottles_left)
    return result

def song(start, stop=0):
    result = ""
    for i in xrange(start, stop - 1, -1):
        result += verse(i) + "\n"
    return result
        