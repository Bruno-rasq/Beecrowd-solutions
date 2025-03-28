nome = input()
dd, dm, da = [int(x) for x in input().split("/")] #dia atual, mes e ano
nd, nm, na = [int(x) for x in input().split("/")] #data nascimento

if nd == dd and nm == dm:
    print("Feliz aniversario!")

idade = da - na
if dm < nm or (dm == nm and dd < nd):
    idade -= 1

print(f"Voce tem {idade} anos {nome}.")