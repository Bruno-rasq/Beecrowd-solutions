class Base32:
    Base = [str(i) for i in range(10)] + [chr(i) for i in range(65, 87)]
    memory = {}
    
    @staticmethod
    def resolve():
        while True:
            decimal = int(input())
            if decimal == 0: print(0); break 
        
            if decimal in Base32.memory:
                print(Base32.memory[decimal])
                continue
            
            def convert_base_to_32(n):
                rest = []
                while n != 0:
                    char = Base32.Base[int(n % 32)]
                    rest.append(char)
                    n = n // 32
                    
                return "".join(rest[::-1])
            
            b32 = convert_base_to_32(decimal)   
            Base32.memory[decimal] = b32
            
            print(b32)
            
Base32.resolve() 