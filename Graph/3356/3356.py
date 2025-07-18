from collections import defaultdict

class Controlled_Breeding:

    @staticmethod
    def DFS(GP, horse, visiteds):
        if horse in visiteds: return
        visiteds.add(horse)
        for child in GP[horse]:
            Controlled_Breeding.DFS(GP, child, visiteds)

    @staticmethod
    def resolve():
        amount_horses, amount_relations, amount_tests = map(int, input().split())

        GP = defaultdict(list)
        for _ in range(amount_relations):
            parentA, parentB, child = input().split()
            GP[parentA].append(child)
            GP[parentB].append(child)

        # Para evitar erro de "dictionary changed size during iteration"
        horses = list(GP.keys())

        ancestry_map = {}  # cavalo → descendentes

        for horse in horses:
            if horse not in ancestry_map:
                visiteds = set()
                Controlled_Breeding.DFS(GP, horse, visiteds)
                ancestry_map[horse] = visiteds


        for _ in range(amount_tests):
            horseA, horseB = input().split()
            RB = False
            for horse in ancestry_map:
                 if horseB in ancestry_map[horse] and horseA in ancestry_map[horse]:
                     RB = True
                     break
            
            print("verdadeiro" if RB else "falso")

Controlled_Breeding.resolve()