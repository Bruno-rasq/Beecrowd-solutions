class Fans_and_Balloons:
    @staticmethod
    def resolve():
        while True:
            r, c, p = [int(x) for x in input().split()]
            if r == c == p == 0: break
            
            output = None
            pos = p - 1
            for row in range(r):
                line = [int(x) for x in input().split()]
                
                fan_left, fan_right = None, None
                l, r = pos, pos 
                while fan_left is None:
                    l -= 1
                    if line[l] != 0: fan_left = l
                    
                while fan_right is None:
                    r += 1
                    if line[r] != 0: fan_right = r
                    
                if line[pos] != 0:
                    print(row, pos + 1)
                    return  
                
                if line[r] > line[l]:
                    pos -= line[r]
                    pos += line[l]
                else:
                    pos -= line[r]
                    pos += line[l]
                    
                if line[pos] != 0:
                    output = f"BOOM {row + 1} {pos + 1}"
                    break 
                    
                output = f"OUT {pos + 1}"
            
            print(output)
                
Fans_and_Balloons.resolve()