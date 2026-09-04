class Generate_Random_Numbers:
    @staticmethod
    def generate(a: str) -> str:
        squared = str(int(a) ** 2).zfill(2 * len(a))
        mid = len(squared) // 2
        return squared[mid-2:mid+2]  # 4 dígitos centrais

    @staticmethod
    def solve(a0: str):
        seen = set()
        curr = a0
        while curr not in seen:
            seen.add(curr)
            curr = Generate_Random_Numbers.generate(curr)
        print(len(seen))


# leitura até "0"
while True:
    n = input().strip()
    if n == "0":
        break
    Generate_Random_Numbers.solve(n)