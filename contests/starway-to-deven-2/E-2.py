n = int(input())

k = n / 2 # numero de termos em pares

sum_pares = k * (k + 1) #soma dos numeros pares

num_impares = (n + 1) // 2

count = sum_pares + num_impares

print(count)