curr = int(input())
ans = 1

while curr >= 2:
    curr = curr / 2
    ans = ans * 4
    
print(ans)