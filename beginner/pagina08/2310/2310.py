numero_dados = int(input())

tentativas_servico = 0
tentativas_bloqueio = 0
tentativas_ataque = 0
servicos_concluidos = 0
bloqueios_concluidos = 0
ataques_concluidos = 0

for _ in range(numero_dados):
    nome = input()
    ts, tb, ta = [int(x) for x in input().split()]
    s, b, a = [int(x) for x in input().split()]

    tentativas_servico += ts
    tentativas_bloqueio += tb
    tentativas_ataque += ta
    servicos_concluidos += s
    bloqueios_concluidos += b
    ataques_concluidos += a 

porcent_s = (servicos_concluidos * 100) / tentativas_servico
porcent_b = (bloqueios_concluidos * 100) / tentativas_bloqueio
porcent_a = (ataques_concluidos * 100) / tentativas_ataque

print(
    f"Pontos de Saque: {porcent_s:.2f} %.",
    f"Pontos de Bloqueio: {porcent_b:.2f} %.",
    f"Pontos de Ataque: {porcent_a:.2f} %.",
    sep="\n"
)