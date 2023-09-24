select 
    name, round(people.salary * 0.10, 2) as tax
from people
where salary >= 3000;