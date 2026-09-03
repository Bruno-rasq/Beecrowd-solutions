def bin_to_dec(binary: str) -> int:
    expo = len(binary) - 1
    decimal = 0
    for digit in binary:
        decimal += int(digit) * (2 ** expo)
        expo -= 1
    return decimal

def dec_to_bin(n: int) -> str:
    if n == 0: return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario

def dec_to_hex(n: int) -> str:
    if n == 0: return "0"
    hex_chars = "0123456789abcdef"
    hexadecimal = ""
    while n > 0:
        resto = n % 16
        hexadecimal = hex_chars[resto] + hexadecimal
        n //= 16
    return hexadecimal

def hex_to_dec(h: str) -> int:
    hex_chars = "0123456789abcdef"
    decimal = 0
    for i, char in enumerate(reversed(h)):
        decimal += hex_chars.index(char) * (16 ** i)
    return decimal

def bin_to_hex(binary: str) -> str:
    while len(binary) % 4 != 0:
        binary = "0" + binary
    hex_chars = "0123456789abcdef"
    hexadecimal = ""
    for i in range(0, len(binary), 4):
        grupo = binary[i:i+4]
        valor = int(grupo, 2)
        hexadecimal += hex_chars[valor]
    return hexadecimal

def hex_to_bin(hexa: str) -> str:
    hex_chars = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "a": "1010", "b": "1011",
        "c": "1100", "d": "1101", "e": "1110", "f": "1111"
    }
    binario = "".join(hex_chars[c] for c in hexa)
    binario = binario.lstrip("0")  # remove zeros à esquerda
    return binario if binario else "0"  # garante que "0" não vire ""

class Base_Conversion:
    @staticmethod
    def solve():
        n_test_cases = int(input())
        
        for i in range(1, n_test_cases + 1):
            val, base = input().split()
            print(f"Case {i}:")
            
            if base == "dec":
                num = int(val)
                print(f"{dec_to_hex(num)} hex")
                print(f"{dec_to_bin(num)} bin")
                
            elif base == "bin":
                num = bin_to_dec(val)
                print(f"{num} dec")
                print(f"{dec_to_hex(num)} hex")
                
            else:  # base == "hex"
                num = hex_to_dec(val)
                print(f"{num} dec")
                print(f"{hex_to_bin(val)} bin")
            
            print()  # linha em branco após cada caso

Base_Conversion.solve()