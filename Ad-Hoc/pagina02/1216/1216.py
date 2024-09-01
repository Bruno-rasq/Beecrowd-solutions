media, pessoa = 0, 0

while True:
  try:
    nome = input()
    dist = int(input())

    media += dist
    pessoa += 1
  except EOFError:
    break 

result = media/pessoa

print(f"{result:.1f}")