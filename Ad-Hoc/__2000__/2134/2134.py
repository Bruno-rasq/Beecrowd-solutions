from collections import defaultdict

instancia = 1
while True:
    try:

        bucket = defaultdict(list)
        num_students = int(input())
        
        for _ in range(num_students):
            name, solve_problems = input().split()
            bucket[int(solve_problems)].append(name)
            
        for problems in sorted(bucket):
            for student in sorted(bucket[problems], reverse=True):
                print(f"Instancia {instancia}")
                print(student)
                break
            break
        print()
        instancia += 1
        
    except EOFError: break