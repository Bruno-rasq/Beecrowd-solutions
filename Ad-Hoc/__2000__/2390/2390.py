amoung_used = int(input())
times = [0] * amoung_used

for i in range(amoung_used):
   times[i] = int(input())
   
def count_time(times):
    idx, time = 0, 0
    while idx < len(times) - 1:
        current_time = times[idx]
        next = times[idx + 1]
        count = 10 
        while True:
            if count <= 0 or next == current_time: break
            current_time += 1
            count -= 1
            time += 1
        idx += 1
    return time + 10
    
print(count_time(times))