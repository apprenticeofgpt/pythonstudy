def is_valid_parentheses(s):
    stack = []
    pair = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack.pop() != pair[ch]:
                return False
    return not stack
print(is_valid_parentheses('({)'))