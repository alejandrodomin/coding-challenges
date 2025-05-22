from enum import unique


def len_longest_sub_string(s: str) -> int:
    s_ptr, e_ptr = 0, 0

    longest = 0
    while e_ptr < len(s):
        window = s[s_ptr:e_ptr]

        if len(set(window)) == len(window):
            e_ptr += 1
            longest = max(longest, len(window))
        else:
            s_ptr += 1

    return longest


if __name__=='__main__':
    text = "pwwkews_pt"

    print(len_longest_sub_string(text))