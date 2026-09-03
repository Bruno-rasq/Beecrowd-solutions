class Primary_arithmetic:
    @staticmethod
    def solve(a: str, b: str):
        max_length = max(len(a), len(b))
        A = a.rjust(max_length, "0")[::-1]
        B = b.rjust(max_length, "0")[::-1]
        
        carrys = 0
        transport = 0
        
        for idx in range(max_length):
            _sum = int(A[idx]) + int(B[idx]) + transport
            if _sum >= 10:
                carrys += 1
                transport = 1 
            else:
                transport = 0 
            
        
        if carrys == 0: out = "No carry operation."
        if carrys == 1: out = "1 carry operation."
        if carrys > 1: out =  f"{carrys} carry operations."
        print(out)
        
while True:
    a, b = input().split()
    if a == b == "0": break 
    
    Primary_arithmetic.solve(a, b)