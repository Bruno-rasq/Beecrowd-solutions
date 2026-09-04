amount_birds, amount_places = [int(x) for x in input().split()]

laps = 0

for _ in range(amount_birds):
    n_escapes, *curr_places = [int(x) for x in input().split()]
    
    places = [0] + curr_places + [0]
    displacement = 0
    
    for i in range(len(places) - 1):
        a = places[i]
        b = places[i + 1]
        if b >= a: 
            displacement += b - a
        else:
            displacement += (amount_places - a) + b
        
    laps = max(laps, displacement // amount_places)
    
print(laps)