SELECT nome, kg 
FROM ingrediente 
WHERE kg > 0.000 AND kg < 10.000 
ORDER BY kg;