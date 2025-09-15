class Where_are_my_keys:
    @staticmethod
    def solve(number_of_offices: int) -> None:
        visited_offices = set([int(x) for x in input().split()])
        
        for _ in range(number_of_offices):
            office = int(input())
            
            print(0 if office in visited_offices else 1)
            visited_offices.add(office)
            
N, Q = [int(x) for x in input().split()]
Where_are_my_keys.solve(N)