select prod.name, prov.name, categ.name 
from products prod inner join providers prov 
on prov.id = prod.id_providers inner join categories categ
on categ.id = prod.id_categories
where prov.name = 'Sansul SA' and categ.name = 'Imported';