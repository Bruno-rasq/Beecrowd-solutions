def maximum_rectangle_can_be_formad(sticks: dict[int, int]) -> int:
    maximum_rectangles = 0
    for stick in sticks:
        maximum_rectangles += sticks[stick] // 2
            
    return maximum_rectangles // 2
    
while True:
    n = int(input())
    
    if n == 0: break
    
    sticks = {}
    for _ in range(n):
        stick, qnt = [int(x) for x in input().split()]
        sticks[stick] = qnt
        
    print(maximum_rectangle_can_be_formad(sticks))