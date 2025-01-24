from enum import Enum
import copy

class Direction(Enum):
    NORTH,EAST,SOUTH,WEST=1,2,3,4

matrix,start=[],None

def parse_input():
    global matrix, start
    input="""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    for r_index, row in enumerate(input.split('\n')):
        row = list(row)
        matrix.append(row)

        if start is None:
            for i_index, item in enumerate(row):
                if item == '^':
                    start=(r_index, i_index)

def walk_matrix():
    global matrix, start
    visited=set()
    direction=Direction.NORTH
    curr_loc=start
    done=False

    while not done:
        visited.add(curr_loc)
        try:
            match direction:
                case Direction.NORTH:
                    new_y = curr_loc[0] - 1
                    if new_y < 0:
                        raise IndexError("out of bounds")
                    elif matrix[new_y][curr_loc[1]] == '#':
                        direction=Direction.EAST
                    else:
                        curr_loc=(new_y, curr_loc[1])

                case Direction.EAST:
                    new_x = curr_loc[1] + 1
                    if new_x < 0:
                        raise IndexError("out of bounds")
                    elif matrix[curr_loc[0]][new_x] == '#':
                        direction=Direction.SOUTH
                    else:
                        curr_loc=(curr_loc[0], new_x)

                case Direction.SOUTH:
                    new_y = curr_loc[0] + 1
                    if new_y < 0:
                        raise IndexError("out of bounds")
                    elif matrix[new_y][curr_loc[1]] == '#':
                        direction=Direction.WEST
                    else:
                        curr_loc=(new_y, curr_loc[1])

                case Direction.WEST:
                    new_x = curr_loc[1] - 1
                    if new_x < 0:
                        raise IndexError("out of bounds")
                    elif matrix[curr_loc[0]][new_x] == '#':
                        direction=Direction.NORTH
                    else:
                        curr_loc=(curr_loc[0], new_x)

        except IndexError:
            done=True

    return visited


def main():
    global matrix, start

    parse_input()
    visited_locs = walk_matrix()

    print(len(visited_locs))

if __name__=="__main__":
    main()
