n = int(input())

for _ in range(n):
    curr = list(input())
    result = []

    for char in curr:
        if char.upper() != char:
            result.append(char)
    
    result.reverse()
    pirnt("".join(result))