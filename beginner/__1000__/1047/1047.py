import math

h1, m1,  h2, m2 = [int(n) for n in input().split()]

if h2 <= h1 and m2 <= m1:
    h2 = h2 + 24

elif m2 <= m1:
    m2 = m2 + 60
    h2 = h2 - 1

s1 = (h1 * 3600) + (m1 * 60) 
s2 = (h2 * 3600) + (m2 * 60)

tempo = s2 - s1
hr = math.floor(tempo / 3600)
min = ((tempo - (hr * 3600)) / 60)

print(f"O JOGO DUROU {hr} HORA(S) E {min:.0f} MINUTO(S)")