import shlex # separa uma string por espaço ou entre aspas
import math

class INPUT:
    def __init__(self, text):
        self.tokens = shlex.split(text)

    def get_data(self):
        return self.tokens.pop(0)
    
test_case = 1
while True:
    data = input()
    if data == "0": break 

    INP = INPUT(data)
    r = int(INP.get_data())
    n = int(INP.get_data())
    ps = [INP.get_data(), INP.get_data()]
    current_p = ps[(math.ceil(r / n) - 1) % len(ps)]
    
    print(f"{test_case}. {current_p.lower()}")
    test_case += 1