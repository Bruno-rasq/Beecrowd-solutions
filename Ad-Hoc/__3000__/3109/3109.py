class Desk_Updates:
    @staticmethod
    def solve(n_employees, q_queries):
        desk = [i for i in range(1, n_employees + 1)]
        
        for _ in range(q_queries):
            querie = [int(x) for x in input().split()]
            
            if querie[0] == 1:
                _, A, B = querie
                desk[A - 1], desk[B - 1] = desk[B - 1], desk[A - 1] # swap A e B
                continue
                
            _, A = querie
            redirects = 0
            current_desk = A
            while desk[current_desk - 1] != A:
                redirects += 1
                current_desk = desk[current_desk - 1]
            print(redirects)


employees = int(input())
queries = int(input())
Desk_Updates.solve(employees, queries)