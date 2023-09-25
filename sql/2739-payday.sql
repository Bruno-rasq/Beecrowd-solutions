select l.name, 
    cast((EXTRACT(DAY FROM payday)) as int) as day 
from loan l;