coords = ["N", "L", "S", "O"]

n = int(input())

while n != 0:
    index = 0
    turns = input()
    for i in range(n):
        if turns[i] == "D":
            index = (index + 1) % len(coords)
        else:
            index = (index - 1) % len(coords)

    print(coords[index])
    n = int(input())
