class Postman:
    @staticmethod
    def solve():
        n_houses, n_deliveries = [int(x) for x in input ().split()]
        houses = [int(x) for x in input ().split()]
        order_deliveries = [int(x) for x in input ().split()]
        idxs = {house: idx for idx, house in enumerate(houses)}
        
        time = 0
        curr_house = houses[0]
        
        for OD in order_deliveries:
            curr_idx = idxs[curr_house]
            next_idx = idxs[OD]
            curr_house = OD
            
            time += abs(curr_idx - next_idx)
            
        print(time)
        
Postman.solve()