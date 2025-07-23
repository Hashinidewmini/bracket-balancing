def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
       print("Hello hello hello")

    return len(stack) == 0  # True if all brackets are closed


# Example Usage
test1 = "{[()]}"
test2 = "{[(])}"
test3 = "(()[]{})"

print(is_balanced(test1))  # ✅ True
print(is_balanced(test2))  # ❌ False
print(is_balanced(test3))  # ✅ True
