def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Índice inicial para o subarray da esquerda
    j = mid + 1 # Índice inicial para o subarray da direita
    k = left    # Índice inicial para o subarray temporário
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # Contagem de inversões
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

n = int(input())
for _ in range(n):
    leng = int(input())
    if leng == 0:
        print("Optimal train swapping takes 0 swaps.")
        continue

    vet = list(map(int, input().split()))
    temp_arr = [0] * leng
    swaps = merge_sort_and_count(vet, temp_arr, 0, leng - 1)
    print(f"Optimal train swapping takes {swaps} swaps.")
