distance_map = {}
visited = []

def valid_moves(coord: tuple[int, int], matrix: list[list[int]]):
    global visited

    row, item = coord
    moves = [(row - 1 , item),
             (row, item - 1),
             (row, item + 1),
             (row + 1, item)]

    max_r, max_i = len(matrix), len(matrix[0])
    v_moves = []
    for x, y in moves:
        if 0 <= x < max_r and 0 <= y < max_i and (x, y) not in visited:
            v_moves.append((x, y))

    visited.extend(v_moves)
    return v_moves


def nearest_0(coord, matrix):
    global distance_map

    if coord not in distance_map:
        if matrix[coord[0]][coord[1]] == 0:
            distance_map[coord] = 0
        else:
            distances = []
            for move in valid_moves(coord, matrix):
                distances.append(nearest_0(move, matrix))

            distance = min(distances) + 1
            distance_map[coord] = distance

    return distance_map[coord]


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
