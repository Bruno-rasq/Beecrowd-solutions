n = int(input())

def to_hex(num):
  if num == 0:
    return "0"

  hex_digits = "0123456789ABCDEF"
  hex_num = ""
  while num > 0:
    hex_num = hex_digits[num % 16] + hex_num
    num = num // 16
  return hex_num

print(to_hex(n))