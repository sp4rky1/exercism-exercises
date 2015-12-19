actions = ['wink', 'double blink', 'close your eyes', 'jump']

def handshake(code):
    if type(code) == int:
        code = bin(code)[2:]
    result = []
    if any(char != '0' and char != '1' for char in code):
        return result
    for index, digit in enumerate(code[::-1]):
        if digit == '1' and index != 4:
            result.append(actions[index])
    if len(code) == 5:
    	result.reverse()
    return result
            
def code(handshake):
    if any(action not in actions for action in handshake):
        return '0'
    result = 0
    if len(handshake) >= 2 and actions.index(handshake[0]) > actions.index(handshake[1]):
        result = 16
    for action in handshake:
        i = actions.index(action)
        result += 2 ** i
    return bin(result)[2:]