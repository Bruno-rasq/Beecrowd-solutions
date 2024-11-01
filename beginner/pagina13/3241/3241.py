n= int(input())

for _ in range(n):
    curr = input()

    if curr == "P=NP":
        print("skipped")
        continue

    a, b = curr.split("+")
    a = int(a)
    b = int(b)
    print(a + b)