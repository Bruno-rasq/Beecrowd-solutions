class Binary_Hexadecimal_Number_Systems:
    @staticmethod
    def isPowerOfTwo(n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
        
n = int(input())
ispot = Binary_Hexadecimal_Number_Systems.isPowerOfTwo(n)
print("true" if ispot else "false")