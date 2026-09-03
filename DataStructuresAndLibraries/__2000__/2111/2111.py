def set_Soroban(n: str) -> None:
    
    soroban_map = {
        "0": "10-01111", "1": "10-10111",
        "2": "10-11011", "3": "10-11101",
        "4": "10-11110", "5": "01-01111",
        "6": "01-10111", "7": "01-11011",
        "8": "01-11101", "9": "01-11110",
    }
    configuracao = [soroban_map[x] for x in n.zfill(9)]

    for i in range(8):
        output = ""
        for fileira in configuracao:
            output += fileira[i]
        print(output)
    print()
    

while True:
    try: set_Soroban(input())
    except EOFError: break