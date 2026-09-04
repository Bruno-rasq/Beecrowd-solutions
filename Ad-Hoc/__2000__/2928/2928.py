N = int(input())
mapping_lake = [input() for _ in range(N)]
mapping_lake.append("----------")
jumps = 0
ans = 0

for line in mapping_lake:
    if jumps > 2: break 
    if "." == line[0]:
        jumps += 1
        continue
    if jumps != 0: ans += 1
    jumps = 0

print(ans if jumps <= 2 else "N")