def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in brackets.values():  # Opening brackets
            stack.append(char)
        elif char in brackets.keys():  # Closing brackets
            if not stack or stack.pop() != brackets[char]:
                return False


    return len(stack) == 0  # True if all brackets are closed


# Example Usage
test1 = "{[()]}"
test2 = "{[(])}"
test3 = "(()[]{})"

print(is_balanced(test1))  # ✅ True
print(is_balanced(test2))  # ❌ False
print(is_balanced(test3))  # ✅ True
