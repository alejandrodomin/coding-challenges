# intuition on this one tells me to just have a 1 carry that we keep adding.

def add_bin(x: str, y: str) -> str:
    if len(x) > len(y):
        big, small = x, y
    else:
        big, small = y, x

    big, small = big[::-1], small[::-1]

    result = []
    for index in range(len(big)):
        if small[index] == "1":
            if big[index] == "1":
                big[index] == "0"

        result.append(big[index])


if __name__ == '__main__':
    add_bin(x, y)
