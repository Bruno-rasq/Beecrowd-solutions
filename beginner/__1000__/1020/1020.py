# ages in days

'''
Leia um valor inteiro correspondente a idade em dias de uma pessoa, e print-a em anos, meses e dias, seguidos respectivamente por “ano(s)”, “mes(es)”, “dia(s)”.
'''

# example 400
# 1 ano(s)
# 1 mes(es)
# 5 dia(s)

age = 400

years = int(age / 365)
mounths = int((age % 365) / 30)
day = int((age % 365) % 30)

print(years, "ano(s)")
print(mounths, "mes(es)")
print(day, "dia(s)")