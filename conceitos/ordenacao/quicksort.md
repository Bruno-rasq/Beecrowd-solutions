# Quick Sort.

**O que é o Quick Sort?** É um algoritmo de ordenação eficiente, do tipo 
dividir para conquistar (divide and conquer), que organiza elementos
de uma lista/array em ordem crescente ou decrescente.

**funcionamento:**

- Pivô: é necessário primeiro escolher um elemento pivô.
- particionar o array/vetor/lista em duas partes.
  - a parte esquerda: elementos menores que o pivô.
  - a parte direita: elementos maiores que o pivô.
  - OBS: em casos de array com valores repetidos é
    criar uma terceira partição para os valores iguais
    ao pivô.
- recursivamente repetir o processo até que cada partição tenha no máximo
  1 elemento.
- por último é necessário unir todas essas partições novamente.


**Por que é rápido?** Na média, faz ordenação em tempo O(n log n), porque 
divide o problema em partes cada vez menores. Mas no pior caso (quando 
o pivô é sempre o maior ou o menor elemento, como em listas já ordenadas) 
pode chegar a O(n²).

**Dica para melhorar:** Se quiser evitar o pior caso, use um pivô aleatório ou 
a técnica do median-of-three (média de três valores) para escolher o pivô.

exemplo em python:

```python

def quicksort(arr):
    if len(arr) <= 1: return arr 
    
    pivo = arr[len(arr) // 2] #-> peguei o elemento do meio
    left, middle, right = [], [], []
    
    for n in arr:
        if n < pivo: left.append(n)
        if n == pivo: middle.append(n)
        if n > pivo: right.append(n)
        
    return quicksort(left) + middle + quicksort(right)

```
