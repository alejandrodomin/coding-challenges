""" 
New and improved runtime:
Runtime 0ms Beats 100.00%
Memory 12.58MB Beats 50.91%
"""

def isValid(s):
    mapping={")":"(", "}":"{", "]":"["}

    stack=[]
    for char in list(s):
        if not stack or char not in mapping:
            stack.append(char)
        elif stack[-1] == mapping[char]:
            stack.pop()
        else:
            return False

    return not stack
    

print(isValid("["))