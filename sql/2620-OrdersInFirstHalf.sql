select customers.name, orders.id 
from customers inner join orders 
on orders.id_customers = customers.id 
where orders.orders_date between '20160101' and'20160630' ;