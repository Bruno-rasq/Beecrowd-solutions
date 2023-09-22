SELECT prod.name, prov.name, prod.price 
FROM products prod INNER JOIN providers prov
ON prod.id_providers = prov.id INNER JOIN categories 
ON prod.id_categories = categories.id 
WHERE prod.price > 1000 AND categories.id = 1;
