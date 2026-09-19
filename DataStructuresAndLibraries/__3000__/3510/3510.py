open_parentheses = 0
open_braces = 0
open_brackets = 0

ans = 0

expression = input()

for char in expression:

    if char == '(':
        open_parentheses += 1

    elif char == ')':
        if open_parentheses > 0:
            open_parentheses -= 1
        else:
            ans += 1

    elif char == '{':
        open_braces += 1

    elif char == '}':
        if open_braces > 0:
            open_braces -= 1
        else:
            ans += 1

    elif char == '[':
        open_brackets += 1

    elif char == ']':
        if open_brackets > 0:
            open_brackets -= 1
        else:
            ans += 1

ans += open_parentheses
ans += open_braces
ans += open_brackets

print(ans)