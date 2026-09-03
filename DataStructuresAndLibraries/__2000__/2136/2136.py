candidados_sim = set()
candidados_nao = set()

amigo_habay = ""
while (entrada := input()) != "FIM":
    nome, voto = entrada.split()
    
    if voto == "NO":  candidados_nao.add(nome)
    if voto == "YES":
        candidados_sim.add(nome)
        if len(nome) > len(amigo_habay):
            amigo_habay = nome
    
output = list(sorted(candidados_sim)) + list(sorted(candidados_nao))

print("\n".join(output))
print()
print("Amigo do Habay:")
print(amigo_habay)