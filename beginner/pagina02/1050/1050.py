tabela_DDD_regiao = {
    "61": "Brasilia",       "71": "Salvador",
    "11": "Sao Paulo",      "21": "Rio de Janeiro",
    "32": "Juiz de Fora",   "19": "Campinas",
    "27": "Vitoria",        "31": "Belo Horizonte"
}

ddd = input()
regiao = tabela_DDD_regiao.get(ddd)
print(regiao if regiao != None else "DDD nao cadastrado")