SELECT
    packages.year AS year, 
    sender.name AS sender,
    receiver.name AS receiver
    
FROM packages
INNER JOIN users sender
ON Packages.id_user_sender = sender.id

INNER JOIN users receiver
ON Packages.id_user_receiver = receiver.id

WHERE (Packages.color ILIKE 'Blue' OR Packages.year >= 2015)
        AND sender.address NOT ILIKE 'Taiwan'
        AND receiver.address NOT ILIKE 'Taiwan'
        
ORDER BY Packages.year DESC, Packages.id_package DESC;