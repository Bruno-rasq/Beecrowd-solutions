n_casos = int(input())

for _ in range(n_casos):
    n = int(input())
    pedidos = []
    
    for _ in range(n):
        objeto, pedido = input().split()
        
        if pedido == "chirrin":
            pedidos.append(objeto)
            continue 
            
        if pedido == "chirrion":
            if objeto in pedidos:
                pedidos.remove(objeto)
                continue
        
    pedidos.sort()
    print("TOTAL")
    print("\n".join(pedidos))