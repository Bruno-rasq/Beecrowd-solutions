class Firmware_Substring_Manipulation:
    @staticmethod
    def remove_occurrences(strg: str, sub: str):

        n, m = len(strg), len(sub)
        i = 0
        pos = -1  # posição onde encontramos a substring
        
        while i <= n - m:
            if strg[i:i+m] == sub:  # verifica se a substring bate
                pos = i
                break
            i += 1
        
        if pos != -1:  # se encontrou
            return Firmware_Substring_Manipulation.remove_occurrences(
                strg[:pos] + strg[pos+m:], sub
            )

        print(strg if len(strg) != 0 else "null value")
            
string, substring = input(), input()
Firmware_Substring_Manipulation.remove_occurrences(
    string, substring
)