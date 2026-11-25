# Serie de leds controlados por um botão:
# Ao clicar no botão o led mais a direita troca de estado.
# ("O" on && "-" off)

# Caso o led apague, o led adjacente esquerdo dele troca de estado.
# Se o led esquerdo ascender então ele propaga a troca até que um
# led se apague.

numberLeds = int(input())
currentConfig = input()
targetConfig = input()

totalClicks = 0

def TOGGLE(led):
    if led == "O": return "-"
    return "O"

while currentConfig != targetConfig:

    totalClicks += 1

    curr = list(currentConfig)

    curr[numberLeds - 1] = TOGGLE(curr[numberLeds - 1])

    if curr[numberLeds - 1] == "-":
        currentLed = numberLeds - 2

        while currentLed >= 0:
            curr[currentLed] = TOGGLE(curr[currentLed])

            if curr[currentLed] == "O":
                break

            currentLed -= 1
            
    currentConfig = "".join(curr)
    
print(totalClicks)