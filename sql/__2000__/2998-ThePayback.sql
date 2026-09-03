select 
    clients.name,
    clients.investment,
CEILING((clients.investment / AVG(DISTINCT operations.profit))) as month_of_payback, 
(SUM(operations.profit) - clients.investment) as return
    
from operations 
inner join clients 
on clients.id = operations.client_id

where operations.month in (1,2,3)
group by clients.id
having (SUM(operations.profit) - clients.investment) >= 0
ORDER BY return desc;