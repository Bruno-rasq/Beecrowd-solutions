n= int(input())

villains = []
for _ in range(n):
    villain = input()

    if villain not in villains:
        villains.append(villain)
        print("Y")
    else:
        print("N")