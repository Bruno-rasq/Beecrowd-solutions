from collections import deque

N = int(input())
stacks = [deque([int(x)]) for x in input().split()]

while True:
    swaps = 0

    i = N - 2
    j = N - 1

    while i >= 0:
        if len(stacks[i]) == 1:
            if not stacks[j] or stacks[i][-1] >= stacks[j][-1]:
                stacks[j].append(stacks[i].pop())
                swaps += 1

        i -= 1
        j -= 1

    if swaps == 0:
        break

print(sum(bool(stack) for stack in stacks))