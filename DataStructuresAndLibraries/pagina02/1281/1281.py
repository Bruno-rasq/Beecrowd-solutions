CASES=int(input())

for _ in range(CASES):
  #quantity of products
  q_of_prod = int(input())

  market = {}
  for _ in range(q_of_prod):
    prod, price = input().split(" ")
    market[prod] = float(price)

  
  len_list = int(input())

  total = 0.0
  for _ in range(len_list):
    item, quantity = input().split(" ")
    total += market[item] * int(quantity)

  
  print(f"R$ {total:.2f}")