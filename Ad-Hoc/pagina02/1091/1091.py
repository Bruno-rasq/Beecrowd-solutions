cases = int(input())

def tolist(s):
    return [int(elemento) for elemento in s.split()]

def location(data):
    cood = tolist(data.pop(0))
    for n in data:
        curr = tolist(n)
        if any(ele in curr for ele in cood):
            print('divisa')
        else:
            cx, cy = cood
            x, y = curr
            if x > cx and y > cy:
                pritn('NE')
            elif x > cx and y < cy:
                print('SE')
            elif x < cx and y < cy:
                print('SO')
            else:
                print('NO')


data = []
while cases != 0:
    for n in range(cases + 1):
        curr = input()
        data.sppend(curr)
    laocation(data)
    data.clear()
    cases = int(input())
