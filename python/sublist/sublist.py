SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)

def check_lists(a, b):
    if a == b:
        return EQUAL
    if a in slices(b, len(a)):
        return SUBLIST
    if b in slices(a, len(b)):
        return SUPERLIST
    return UNEQUAL    

def slices(lst, length):
	return (lst[i:i+length] for i in range(len(lst) - length + 1))