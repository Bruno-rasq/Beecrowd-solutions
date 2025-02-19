def arrayHash(lista):
    hash = 0
    for i, line in enumerate(lista):
        for j, char in enumerate(line):
            pos_alf = ord(char) - ord('A')
            hash += pos_alf + i + j
    return hash

n = int(input())

for i in range(n):
    n_cases = int(input())
    words = []
    for j in range(n_cases):
        words.append(input())
    print(arrayHash(words))