def hex_to_dec(hexadecimal):
    letters = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    
    decimal = 0
    pot = len(hexadecimal) - 1
    for char in hexadecimal:
        integer = None
        if char in letters:integer = letters[char]
        else: integer = int(char)
            
        decimal += integer * (16**pot)
        pot -= 1 
        
    return decimal

class The_Martian:
    @staticmethod
    def translate_hexadecinal_to_ASCII(msg: list[str]):
        out = ""
        for hex_char in msg:
            decimal = hex_to_dec(hex_char)
            out += chr(decimal)
            
        print(out)
        
n_chars = int(input())
hex_msg = [str(x) for x in input().split()]
The_Martian.translate_hexadecinal_to_ASCII(hex_msg)