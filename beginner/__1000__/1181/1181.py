line=int(input()) 
operation=input()

COLUMNS=12
current_line=0
count=0

soma = 0.0

while True:
  try:
    current_number = float(input())
    if current_line != line:
      count = count + 1
      if count == COLUMNS:
        current_line = current_line + 1
        count = 0
        
    else:
      soma += current_number
      count = count + 1
      if count == COLUMNS:
        break
      
  except EOFError:
    break

if operation == "S":
  print(f'{soma:.1f}')
else:
  print(f'{soma/12:.1f}')