
while True:
    try:
        Times = int(input())
        boots_left = []
        boots_right = []
        for i in range(Times):
            T, L = input().split(' ')
            T = int(T)
            curr = {
                "size": T,
                "LR": L
            }
            if L == "D":
                boots_right.append(
                    curr
                )
            else:
                boots_left.append(
                    curr
                )
                
        print(boots_left)
        print(boots_right)
 
    except EOFError:
        break
