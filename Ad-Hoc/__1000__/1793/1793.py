def Count_time(times) -> None:
    idx = 0 
    time = 0
    
    while idx < len(times) - 1:
        current = times[idx]
        next = times[idx + 1]
        count = 10
        
        while True:
            if count <= 0 or current == next: break
            current += 1
            count -= 1
            time += 1
        idx += 1
        
    print(time + 10)
    
while True:
    n = int(input())
    if n == 0: break 

    times = [int(x) for x in input().split()]
    Count_time(times)