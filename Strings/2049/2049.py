class Numbers_of_Ahmoc:
    @staticmethod
    def sliding_window(signature, painel):
        for i in range(len(painel) - len(signature) + 1):
            if painel[i:i+len(signature)] == signature:
                return True
        return False

i = 1
while True:
    signature = input()
    if signature == "0":
        break

    painel = input()
    if i > 1:
        print()
    print(f"Instancia {i}")
    print("verdadeira" if Numbers_of_Ahmoc.sliding_window(signature, painel) else "falsa")
    i += 1