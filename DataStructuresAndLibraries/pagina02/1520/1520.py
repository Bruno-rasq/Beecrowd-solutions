from collections import defaultdict

while True:
    try: N = int(input())
    except EOFError: break
    except: continue

    freq = defaultdict(int)
    for _ in range(N):
        i, f = map(int, input().split())
        for j in range(i, f + 1):
            freq[j] += 1

    try: componente = int(input())
    except: continue

    if componente not in freq:
        print(f"{componente} not found")
        continue

    # Agora, vamos "simular" o rack ordenado:
    pos = 0
    start = -1
    end = -1

    for value in sorted(freq):
        count = freq[value]
        if value == componente:
            start = pos
            end = pos + count - 1
            break
        pos += count

    print(f"{componente} found from {start} to {end}")