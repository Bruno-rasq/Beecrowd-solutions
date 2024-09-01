CASES = int(input())

for _ in range(CASES):
  word = input()
  segundos = len(word) / 100
  print(f"{segundos:.2f}")