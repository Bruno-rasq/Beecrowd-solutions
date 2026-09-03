import struct

var_int = 0
var_real = 0.0
var_str = ''
var_frase = ''

valores = input()

lista = valores.split(' ')
var_int = int(lista[0])
var_real = float(lista[1])
var_str = lista[2]
var_frase = lista[3:]

# Ajustar precisão do float para simples precisão (32 bits) como no enunciado
var_real = struct.unpack('f', struct.pack('f', var_real))[0]

# Juntar a frase (se for mais de uma palavra)
if len(var_frase) > 1:
    s = ' '.join(var_frase)
else:
    s = str(var_frase[0]) if var_frase else ''

# Primeira linha: como lido, separados por espaços simples
print('{}{:.6f}{}{}'.format(var_int, var_real, var_str, s))

# Segunda linha: separados por tabulação (8 espaços) simulada com \t
print("%d\t%.6f\t%c\t%s" % (var_int, var_real, var_str, s))

# Terceira linha: separados por largura fixa de 10, alinhados à direita com espaços à esquerda
print("%10d%10.6f%10c%10s" % (var_int, var_real, var_str, s))