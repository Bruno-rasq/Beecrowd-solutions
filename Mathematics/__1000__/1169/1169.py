class Grains_in_a_Chess_Board:
    @staticmethod
    def resolve():
        n = int(input())
        for _ in range(n):
            squares = int(input())
            grains = 2 ** squares
            kg = grains // 12 // 1000
            print(f"{kg} kg")

Grains_in_a_Chess_Board.resolve()