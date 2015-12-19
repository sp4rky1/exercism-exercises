def board(lines):
    result = [[char for char in row] for row in lines]
    height = len(result)
    width = len(result[0])
    if any(len(row) != width for row in result):
        raise ValueError('Invalid board: not all rows are of same length.')
    corners = [(0, 0), (0, height -1), (width - 1, 0), (width - 1, height - 1)]
    for (i, j) in corners:
        if result[j][i] != '+':
            raise ValueError('Invalid board: faulty border.')
    for i in range(1, width - 1):
        if result[0][i] != '-' or result[height - 1][i] != '-':
            raise ValueError('Invalid board: faulty border.')
    for j in range(1, height - 1):
        if result[j][0] != '|' or result[j][width - 1] != '|':
            raise ValueError('Invalid board: faulty border.')
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            value = result[y][x]
            if value == ' ':
                count = 0
                for j in [y-1, y, y+1]:
                    for i in [x-1, x, x+1]:
                        if result[j][i] == '*':
                            count += 1
                if count:
                    result[y][x] = str(count)
            elif value != '*':
                    raise ValueError('Invalid board: invalid character.')
    return [''.join(row) for row in result]
