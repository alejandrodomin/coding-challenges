""" 
Runtime 43ms Beats 5.10%
Memory 12.35MB Beats 91.80%
"""

def isValid(string):
    types=["()", "[]", "{}"]

    done=False
    while not done:
        done=True

        for tp in types:
            if tp in string:
                string = string.replace(tp, "")
                done=False

    if len(string) > 0:
        return False
    else:
        return True

print(isValid("(]"))