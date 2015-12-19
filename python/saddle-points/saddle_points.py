def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Matrix must be a regular matrix.")
    result = set()
    for i, row in enumerate(matrix):
        column_indices = [column for column, value in enumerate(row) if value == max(row)]
        for index in column_indices:
            if min(row[index] for row in matrix) == max(row):
                result.add((i, index))
    return result