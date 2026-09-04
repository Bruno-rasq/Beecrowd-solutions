class Training_List:
    @staticmethod
    def resolve(n: int, arr: list[int]) -> None:
        _sum = 0
        for i in range(n):
            if arr[i] == 1: _sum += 1
            
        print(_sum)
        
n = int(input())
arr = [int(x) for x in input().split()]
Training_List.resolve(n, arr)