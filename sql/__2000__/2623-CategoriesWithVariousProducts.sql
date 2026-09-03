select prod.name, categ.name 
from products prod inner join categories categ
on categ.id = prod.id_categories
where categ.id in (1, 2, 3, 6, 9) and prod.amount > 100
order by categ.id asc;