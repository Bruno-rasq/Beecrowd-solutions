DIGITOS = ["0", "1"]

_nivel_exclusao = int(input())
_file_original_ = input()
_file_rescrito_ = input()

for i, digit in enumerate(_file_original_):
    idx = 0 if digit == "0" else 1
    if _file_rescrito_[i] != DIGITOS[(idx + _nivel_exclusao) % 2]:
        print("Deletion failed")
        break
else:
    print("Deletion succeeded")