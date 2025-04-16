import re
import pdb

def is_palindrome(s):
    only_letters = re.findall("([A-Za-z0-9]+)", s)
    no_spaces = "".join(only_letters).lower()

    if no_spaces == no_spaces[::-1]:
        return True
    else:
        return False


if __name__=='__main__':
    input="A man, a plan, a canal: Panama"
    print(is_palindrome(input))
