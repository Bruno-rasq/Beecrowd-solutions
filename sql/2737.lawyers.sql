(SELECT name, customers_number
 FROM lawyers
 WHERE customers_number = 
    (SELECT MAX(customers_number) FROM lawyers) OR
    customers_number = 
    (SELECT MIN(customers_number) FROM lawyers)
 ORDER BY
    customers_number DESC)

UNION ALL

SELECT 'Average', ROUND(AVG(customers_number), 0)
FROM lawyers