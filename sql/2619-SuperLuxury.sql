select prod.name, prov.name, prod.price 
from products prod inner join providers prov
on prov.id = prod.id_providers 
inner join categories cate 
on prod.id_categories = cate.id
where cate.name = 'Super Luxury' and prod.price > 1000;