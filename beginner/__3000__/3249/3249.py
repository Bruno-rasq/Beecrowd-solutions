n = int(input())
wins = 0

for i in range(n):
    curr = input()
    if not "CD" in curr:
        wins += 1

print(wins)