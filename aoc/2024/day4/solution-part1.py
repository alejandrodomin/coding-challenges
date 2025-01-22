puzzle=None

def init_puzzle():
    global puzzle
    puzzle="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    puzzle = [list(row) for row in puzzle.split("\n")]

def valid_moves(row, column):
    valid=[]

    valid.append([(row, column + 1), (row, column + 2), (row, column + 3)])             # right
    valid.append([(row + 1, column + 1), (row + 2, column + 2), (row + 3, column + 3)]) # down right diagonal
    valid.append([(row + 1, column), (row + 2, column), (row + 3, column)])             # down
    valid.append([(row + 1, column - 1), (row + 2, column - 2), (row + 3, column - 3)]) # down left diagonal
    valid.append([(row, column - 1), (row, column - 2), (row, column - 3)])             # left
    valid.append([(row - 1, column - 1), (row - 2, column - 2), (row - 3, column - 3)]) # up left diagonal
    valid.append([(row - 1, column), (row - 2, column), (row - 3, column)])             # up
    valid.append([(row - 1, column + 1), (row - 2, column + 2), (row - 3, column + 3)]) # up right diagonal

    return valid

def get_item(row_index, column_index):
    global puzzle

    if row_index < 0 or column_index < 0:
        raise IndexError("No negative values allowed here")

    return puzzle[row_index][column_index]

def main():
    global puzzle
    init_puzzle()
    count=0

    for r_index, row in enumerate(puzzle):
        for c_index, item in enumerate(row):
            if item == 'X':
                valid = valid_moves(r_index, c_index)
                for move in valid:
                    try:
                        if get_item(move[0][0],move[0][1]) == 'M' and get_item(move[1][0],move[1][1]) == 'A' and get_item(move[2][0],move[2][1]) == 'S':
                            count+=1
                    except IndexError:
                        # do nothing
                        continue

    print(count)

if __name__=="__main__":
    main()
