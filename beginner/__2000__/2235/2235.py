# valores dos créditos
c1, c2, c3 = [int(x) for x in input().split()]

def teste1(a, b, c):
    return a + b == c or a + c == b or b + c == a

def teste2(a, b, c):
    return a == b or a == c or b == c

if teste1(c1, c2, c3) or teste2(c1, c2, c3):
    print("S")
else:
    print("N")