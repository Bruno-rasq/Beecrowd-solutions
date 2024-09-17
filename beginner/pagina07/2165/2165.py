text = list(input())
tamanho = len(text)

if tamanho <= 140:
    print('TWEET')
else:
    print('MUTE')