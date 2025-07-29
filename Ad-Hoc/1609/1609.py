class Counting_sheep:
    @staticmethod
    def resolve():
        number_test_cases = int(input())
        for _ in range(number_test_cases):
            number_sheeps = int(input())
            sheeps = set([int(x) for x in input().split()])
            print(len(sheeps))
            
Counting_sheep.resolve()
