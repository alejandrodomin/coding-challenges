def valid_moves(row, item, matrix):
    moves = [[row - 1, item],
             [row, item - 1],
             [row, item + 1],
             [row + 1, item]]

    v_moves = []
    for index, move in enumerate(moves):
        i, j = move
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            v_moves.append(moves[index])

    return v_moves

def nearest_0(i, j, matrix):
    if matrix[i][j] == 0:
        return 0

    moves = []
    for x, y in valid_moves(i, j, matrix):
        if matrix[i][j] == 0:
            # moves.a
            pass

    return min(moves)

def distance_matrix(matrix):
    dis_matrix = [[None] * len(matrix[0])] * len(matrix)

    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            dis_matrix[i][j] = nearest_0(i, j, matrix)

    return dis_matrix


if __name__ == '__main__':
    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

    for row in distance_matrix(matrix):
        print(row)