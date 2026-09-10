SELECT
    node_id,
    CASE
        WHEN COUNT(pointer) = 0 THEN 'LEAF'

        WHEN node_id NOT IN (
            SELECT pointer
            FROM Nodes
            WHERE pointer IS NOT NULL
        ) THEN 'ROOT'

        ELSE 'INNER'
    
    END AS type
FROM Nodes
GROUP BY node_id
ORDER BY node_id;