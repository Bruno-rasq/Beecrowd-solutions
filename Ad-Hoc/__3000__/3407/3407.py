outputs = ["Tudo certo.", "Pegou de Samuel.", "Pegou de um estranho."]

qnt_itens, qnt_cupcakes = [int(x) for x in input().split()]

#qnt_cupcakes_nathan -> qcn && qnt_cupcakes_samuel -> qcs
qcn = sum([int(x) for x in input().split() if x == "1"])
qcs = sum([int(x) for x in input().split() if x == "1"])

if qcn == qcs == qnt_cupcakes: print(outputs[0])
elif qcs > qcn: print(outputs[1])
else: print(outputs[2])