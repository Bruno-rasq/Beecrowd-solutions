while True:

    n_patinhos = int(input())

    if n_patinhos == -1:
        break

    print(n_patinhos - 1 if n_patinhos > 0 else 0)