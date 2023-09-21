select prod.name, forn.name 
from products prod inner join providers forn 
    on prod.id_providers = forn.id
    where prod.id_categories = 6;