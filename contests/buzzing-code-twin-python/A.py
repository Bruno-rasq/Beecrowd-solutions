lista_atual = input().split()
nova_lista  = input().split()
amigo_indicado = input()

lista_atualizada = []
if amigo_indicado != "nao" and amigo_indicado in lista_atual:
    for amigo in lista_atual:
        if amigo == amigo_indicado:
            for novo_amigo in nova_lista:
                lista_atualizada.append(novo_amigo)
        lista_atualizada.append(amiigo)
else:
    lista_atualizada = lista_atual + nova_lista

print(" ".join(lista_atualizada))