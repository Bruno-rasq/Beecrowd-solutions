select prod.name, prov.name 
from products prod inner join providers prov
on prov.id = prod.id_providers 
where prov.name = 'Ajax SA';