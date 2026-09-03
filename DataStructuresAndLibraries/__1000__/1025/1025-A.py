import bisect

i = 1
while True:
    n, q = map(int, input().split())
    if n == 0 and q == 0:
        break

    bolinhas_gude = [int(input()) for _ in range(n)]
    bolinhas_gude.sort()

    querys = [int(input()) for _ in range(q)]

    print(f"CASE# {i}:")

    for query in querys:
        idx = bisect.bisect_left(bolinhas_gude, query)
        if idx < len(bolinhas_gude) and bolinhas_gude[idx] == query:
            print(f"{query} found at {idx + 1}")
        else:
            print(f"{query} not found")
    
    i += 1