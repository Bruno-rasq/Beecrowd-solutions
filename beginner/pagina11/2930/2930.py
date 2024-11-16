entraga, prazo = [int(n) for n in input().split()]

if prazo - entraga >= 1:
    print("Muito bem!, Apresenta antes do Natal!")

elif prazo - entraga < 0:
    print("Eu te odeio professora!")

elif prazo - entraga < 3:
    print("Parece o trabalho do meu filho!")
    prazo += 2
    if prazo <= 24:
        print("TCC Apresentado!")
    else:
        print("Fail! Entao eh nataaaaal!")