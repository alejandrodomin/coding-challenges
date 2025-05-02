distance_map = {}
visited = []

def valid_moves(coord: tuple[int, int]):
    global visited

    row, item = coord
    # TODO: change these to tuples since they can't be added to the distance map
    moves = [[row - 1 , item],
             [row, item - 1],
             [row, item + 1],
             [row + 1, item]]

    v_moves = []
    for move in moves:
        # TODO: check for bounds violations
        if move not in visited:
            v_moves.append(move)

    visited.extend(v_moves)
    return v_moves


def nearest_0(coord, matrix):
    global distance_map

    if coord in distance_map:
        return distance_map[coord]

    if matrix[coord[0]][coord[1]] == 0:
        distance_map[coord] = 0
        return distance_map[coord]

    distances = []
    for move in valid_moves(coord):
        distances.append(nearest_0(move, matrix))

    return min(distances) + 1


def distance_matrix(matrix):
    import copy
    updated_matrix = copy.copy(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            updated_matrix[i][j] = nearest_0((i, j), matrix)

    return updated_matrix


if __name__ == '__main__':
    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

    for row in distance_matrix(matrix):
        print(row)
