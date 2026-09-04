while True:
    N = int(input())
    if N == 0:
        break

    students = [int(x) for x in input().split()]
    idx = int(input()) - 1

    while students[idx] - 1 != idx:
        idx = students[idx] - 1

    print(idx + 1)