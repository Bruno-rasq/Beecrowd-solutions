class Binary_Phrase:
    @staticmethod
    def bin_to_dec(binary: str) -> int:
        decimal = 0
        power = len(binary) - 1
        for digit in binary.strip():
            decimal += (int(digit) * (2 ** power))
            power -= 1
        return decimal

    @staticmethod
    def resolve():
        while True:
            try:
                line = input().strip()
                if not line:  # ignora linhas vazias
                    continue
                    
                msg_size = int(line)
                msg = ""
                for _ in range(msg_size):
                    binary = input().strip()
                    dec = Binary_Phrase.bin_to_dec(binary)
                    msg += chr(dec)
                    
                print(msg)
                
            except EOFError:break
        
Binary_Phrase.resolve()