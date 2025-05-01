while True:
    try:
        traducao = {}

        tamanho_cifra, numero_mensagens = [int(x) for x in input().strip().split()]

        decript = input()
        cript = input()

        lower_decript = decript.lower()
        lower_cript = cript.lower()

        for i in range(tamanho_cifra):
            # Tabela direta
            traducao[cript[i]] = decript[i]
            traducao[lower_cript[i]] = lower_decript[i]
            # Tabela reversa
            traducao[decript[i]] = cript[i]
            traducao[lower_decript[i]] = lower_cript[i]

        for _ in range(numero_mensagens):
            mensagem_cifrada = input()
            for caractere in mensagem_cifrada:
                print(traducao.get(caractere, caractere), end='')
            print('')
        print('')

    except EOFError:
        break