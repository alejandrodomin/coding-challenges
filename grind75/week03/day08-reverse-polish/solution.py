# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9


def reverse_polish(tokens: list[str]) -> float:
    stack = []

    for item in tokens:
        if item.lstrip("-").isdigit():
            stack.append(float(item))
        else:
            b, a = stack.pop(), stack.pop()
            match item:
                case "+":
                    stack.append(a + b)
                case "*":
                    stack.append(a * b)
                case "/":
                    stack.append(a / b)
                case "-":
                    stack.append(a - b)

    return stack[0]


if __name__=='__main__':
    tokens = ["2","1","+","3","*"]

    val = reverse_polish(tokens) 
    print(val)

