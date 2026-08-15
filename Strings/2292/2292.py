import math

# X 5 -> O X O X O ---- (5 / 2) valor truncado 2.5 -> 2
# O 5 -> X O X O X ---- (5 / 2) valor arredondado para cima. 2.5 -> 3

# X 3 -> O X O --- (3 / 2) -> 1.5 (TRUNCANDO) -> 1
# O 3 -> X O X --- (3 / 2) -> 1.5 (arredondado) -> 2

def END_LED_STATE(LEDS, steps):
    # LED mais a esquerda vai apagar N_Toggles vezes... isso indica que os demais
    # leds vão mudar de estado N_Toggles vezes.
    def N_toggles(led, steps):
        return math.trunc(steps / 2) if led == 'X' else math.ceil(steps / 2)
    
    # 0 == X    1 == O
    # X 13 -> O X O X O X O X O X O X O
    # O 13 -> X O X O X O X O X O X O X
    def Toggle(led, steps):
        STATES = ['X', 'O']
        on_off = 0 if led == 'X' else 1
        state = (on_off + steps) % len(STATES)
        return STATES[state]
        
    # O N-esimo led pisca N vezes, dessas N vezes X vezes ele vai apagar, X será 
    # a quantidade de vezes que o próximo led vai piscar... repete o prpcesso.
    ANS = ""
    for idx in range(len(LEDS)):
        curr_led = LEDS[idx]
        ANS += Toggle(curr_led, steps)
        steps = N_toggles(curr_led, steps)
        
    print(ANS)


N = int(input())
for _ in range(N):
    LEDs, steps = input().split()
    END_LED_STATE(LEDs, int(steps))