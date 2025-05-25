def compara_strings(a: str, b: str) -> bool:
    len_str = 3
    for i in range(len_str):
        if a[i] < b[i]: return True
        if a[i] > b[i]: return False
    return len(a) < len(b)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if not compara_strings(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

while True:
    try:
        pacote = input().strip()
        if pacote == "1":
            pacotes_TCP = []
            pacote_tcp = input().strip()
            
            while pacote_tcp != "0":
                _, numero = pacote_tcp.split()
                pacotes_TCP.append(numero)
                pacote_tcp = input().strip()
                
            bubble_sort(pacotes_TCP)
            
            pacotes_TCP = ["Package " + pacote for pacote in pacotes_TCP]
            print("\n".join(pacotes_TCP))
            print("")
    except EOFError:
        break