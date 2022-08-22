def toPostfix(s: str) -> str:
    stack, ans = [], ''

    for char in s:
        if char.isalpha():
            ans += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        elif char == '+' or char == '-':
            while stack and stack[-1] not in '(':
                ans += stack.pop()
            stack.append(char)
        else:
            while stack and stack[-1] in '*/':
                ans += stack.pop()
            stack.append(char)

    while stack:
        ans += stack.pop()

    return ans
    

s = input()
print(toPostfix(s))