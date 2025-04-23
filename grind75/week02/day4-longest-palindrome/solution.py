# this feels like a is this closing bracket correct problem

def longest_palindrom(char_arr: str) -> int:
    char_map = {}

    for char in char_arr:
        if char not in char_map:
            char_map[char] = 0

        char_map[char] += 1

    exception = True
    count = 0
    for key in char_map:
        if char_map[key] % 2 == 0:
            count += char_map[key]
        else:
            count += char_map[key] - 1

            if exception:
                count += 1
                exception = False

    return count


if __name__ == '__main__':
    palindrome = "ccc"
    print(longest_palindrom(palindrome))
