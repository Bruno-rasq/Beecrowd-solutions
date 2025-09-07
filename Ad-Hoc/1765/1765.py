class Christmas_Trapeziums:
    @staticmethod
    def Ice_Cream_Used(Q, A, B):
        ICU = (((A + B) * 5) / 2) * Q 
        return f"Ice Cream Used: {ICU:.02f} cm2"
        
while True:
    test_cases = int(input())
    if test_cases == 0: break 

    case = 1 
    for _ in range(test_cases):
        print("Size #" + str(case) + ":")
        Q, A, B = [float(x) for x in input().split()]
        print(Christmas_Trapeziums.Ice_Cream_Used(Q, A, B))
        case += 1
    print()