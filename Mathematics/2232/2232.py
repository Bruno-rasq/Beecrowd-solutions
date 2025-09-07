#criando o triângulo de pascal com 31 linhas
PT = [[1], [1, 1]]
while len(PT) <= 31:
    last = PT[-1]
    new_line = [1]
    for i in range(len(last) - 1):
        a, b = last[i], last[i + 1]
        new_line.append(a + b)
    new_line.append(1)
    PT.append(new_line)
        

class Pascals_triangle:
    @staticmethod
    def sum_of_the_first_N_lines(n: int) -> None:
        out = 0
        for i in range(n):
            out += sum(PT[i])
        print(out)
        
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    Pascals_triangle.sum_of_the_first_N_lines(n)
    
    
    