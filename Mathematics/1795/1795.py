TT = [[1], [1, 1, 1]]
while len(TT) <= 20:
    last = TT[-1]
    new_line = [1]
    for i in range(len(last)):
        prev = 0 if i == 0 else last[i - 1]
        curr = last[i]
        nex = 0 if i == len(last) - 1 else last[i + 1]

        new_line.append(prev + curr + nex)
    new_line.append(1)
    TT.append(new_line)
    

class Trinomial_Triangle:
    @staticmethod
    def sum_of_all_elements_at_row_R(R: int) -> None:
        out = sum(TT[R])
        print(out)
        

n = int(input())
Trinomial_Triangle.sum_of_all_elements_at_row_R(n)