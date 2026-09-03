def register_student(year) -> str:
    student_name = [word for word in input().split()]
    acronym = "".join([word[0] for word in student_name])
    return acronym + year
    
while True:
    try:
        n, year = [data for data in input().split()]
        system_data = {}
        for _ in range(int(n)):
            key = register_student(year)
            system_data[key] = system_data.get(key, 0) + 1
        ans = 0
        for value in system_data.values():
            if value >= 2: ans += (value - 1)
        print(ans)
    except EOFError: break