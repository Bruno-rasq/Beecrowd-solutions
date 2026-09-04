def input_list():
    return [int(x) for x in input().split()]

while True:
    bancos, debenturas = input_list()
    
    if bancos == 0 and debenturas == 0:
        break 
    
    reservas_monetarias = input_list()

    for _ in range(debenturas):  # Corrigido para ler o número correto de transações
        devedor, credor, valor = input_list()
        reservas_monetarias[devedor - 1] -= valor  # Devedor perde dinheiro
        reservas_monetarias[credor - 1] += valor  # Credor ganha dinheiro
    
    # Verifica se algum banco ficou com saldo negativo
    print("S" if all(reserva >= 0 for reserva in reservas_monetarias) else "N")