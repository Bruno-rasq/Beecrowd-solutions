import sys

class Erasing_and_Winning:
    @staticmethod
    def resolve():
        lines = sys.stdin.read().splitlines()
        idx = 0
        
        while idx < len(lines):
            n, m = map(int, lines[idx].split())
            idx += 1
            if n == m == 0:
                break
            
            nums = lines[idx].strip()
            idx += 1
            
            stack = []
            to_remove = m
            
            for digit in nums:
                while to_remove > 0 and stack and stack[-1] < digit:
                    stack.pop()
                    to_remove -= 1
                stack.append(digit)
            
            # Se ainda restam remoções, corta do final
            result = ''.join(stack[:len(stack)-to_remove])
            
            print(result)
            
Erasing_and_Winning.resolve()