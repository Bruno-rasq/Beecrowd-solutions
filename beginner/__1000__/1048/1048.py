
table_salary_readjustment_rate = {
    #ini        #end            #% 
    (0,         400.00,         15),
    (400.01,    800.00,         12),
    (800.01,    1200.00,        10),
    (1200.01,   2000.00,        7),
    (2000.01,   float('inf'),   4),
}

salary = float(input())

for line in table_salary_readjustment_rate:
    if line[0] <= salary <= line[1]:
        percentual = line[2]
        reajustment = (salary * percentual) / 100.0

        print(f"Novo salario: {(salary + reajustment):.2f}")
        print(f"Reajuste ganho: {reajustment:.2f}")
        print(f"Em percentual: {percentual} %")