select cust.name 
from customers cust inner join legal_person lp
on lp.id_customers = cust.id