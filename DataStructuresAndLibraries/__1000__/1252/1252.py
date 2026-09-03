from collections import defaultdict

class Sort_Sort_and_Sort:
    @staticmethod
    def resolve():  # -> O(N²)
        while True:
            n, MOD = [int(x) for x in input().split()]

            if n == MOD == 0:
                print("0 0")
                break

            nums = defaultdict(lambda: defaultdict(list))

            for _ in range(n):  # -> O(N)
                x = int(input())
                
                # Corrigir o % para comportamento de C
                mod = x % MOD
                if x < 0 and mod != 0:
                    mod -= MOD

                par_impar = 1 if x % 2 == 0 else 0  # par = 1, ímpar = 0
                nums[mod][par_impar].append(x)

            print(f"{n} {MOD}")
            for mod in sorted(nums):  # -> O(N)
                for paridade in sorted(nums[mod]):
                    rev = True if paridade == 0 else False
                    nums[mod][paridade].sort(reverse=rev)
                    for x in nums[mod][paridade]:
                        print(x)
                
Sort_Sort_and_Sort.resolve()