employee = input()
salary = float(input())
sales = float(input())

bonus = (sales * 15) / 100
salaryWithBonus = salary + bonus

print(f"TOTAL = R$ {salaryWithBonus:.2f}")