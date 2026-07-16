sentense = input()
ptr1 = 0
ptr2 = len(sentense) - 1
isPalindrome = True

while ptr1 != ptr2:
    if sentense[ptr1] != sentense[ptr2]:
        isPalindrome = False
        break
    ptr1 += 1
    ptr2 -= 1

if isPalindrome:
    print(f"A frase [{sentense}] eh palindrome")
else:
    print(f"A frase [{sentense}] nao eh palindrome")
    