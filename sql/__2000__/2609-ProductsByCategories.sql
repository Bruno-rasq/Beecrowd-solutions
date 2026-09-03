select categ.name, sum(prod.amount)
from categories categ inner join products prod
on prod.id_categories = categ.id
group BY categ.name