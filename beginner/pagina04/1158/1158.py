def resolve(x, y):
    i = 0
    vector = []
    if x % 2 == 0:
        x += 1
    while i < y:
        vector.append(x)
        i+=1
        x+=2
    print(sum(vector))

j = 0
N = int(input())
while j < N:
    X,Y = input().split(' ')
    X = int(X)
    Y = int(Y)
    resolve(X, Y)
    j+=1