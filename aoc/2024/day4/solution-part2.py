import pdb

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

def get_item(row_index, column_index):
    global puzzle

    if row_index < 0 or column_index < 0:
        raise IndexError("No negative values allowed here")

    return puzzle[row_index][column_index]

def main():
    global puzzle
    init_puzzle()

    allowed_values = ('MAS', 'SAM')
    count=0

    for r_index, row in enumerate(puzzle):
        for c_index, item in enumerate(row):
            if item == 'A':
                try:
                    # top left, top right, bottom left, bottom right
                    top_left = get_item(r_index - 1, c_index - 1)
                    top_right = get_item(r_index - 1, c_index + 1)
                    bottom_left = get_item(r_index + 1, c_index - 1)
                    bottom_right = get_item(r_index + 1, c_index + 1)

                    first_combo = top_left + item + bottom_right
                    second_combo = top_right + item + bottom_left 

                    if first_combo in allowed_values and second_combo in allowed_values:

                        count+=1
                except IndexError:
                    # do nothing
                    continue

    print(count)

if __name__=="__main__":
    main()
