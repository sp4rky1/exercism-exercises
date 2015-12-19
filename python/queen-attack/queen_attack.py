def check_board_validity(white, black):
    values = [white[0], white[1], black[0], black[1]]
    if any(value < 0 or value > 7 for value in values):
        raise ValueError('Invalid coordinates: position is off the board.')
    if white == black:
        raise ValueError('Invalid coordinates: two queens cannot be at the same location.')

def board(white, black):
    check_board_validity(white, black)
    result = ['________'] * 8
    letter = 'WB'
    for i, coord in enumerate([white, black]):
        row = [char for char in result[coord[0]]]
        row[coord[1]] = letter[i]
        result[coord[0]] = ''.join(row)
    return result

def can_attack(white, black):
    check_board_validity(white, black)
    return white[0] == black[0] or white[1] == black[1] or abs(white[0] - black[0]) == abs(white[1] - black[1])