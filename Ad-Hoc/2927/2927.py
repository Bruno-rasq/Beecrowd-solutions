STU, COM, BUR, NCP = map(int, input().split())

functional = COM - BUR - NCP
needed = STU + 1

if functional >= needed:
    print("Igor feliz!")
elif BUR > NCP / 2:
    print("Caio, a culpa eh sua!")
else:
    print("Igor bolado!")