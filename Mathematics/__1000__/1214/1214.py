class Above_Average:
    @staticmethod
    def percentAboveAverage(grades) -> None:
        average = sum(grades) / len(grades)
        count_average_grades = len([grade for grade in grades if grade > average])
        
        PAA = (100 * count_average_grades) / len(grades)
        print(f"{PAA:.3f}%")
        
n_test_cases = int(input())
for _ in range(n_test_cases):
    n, *grades = [int(x) for x in input().split()]
    Above_Average.percentAboveAverage(grades)