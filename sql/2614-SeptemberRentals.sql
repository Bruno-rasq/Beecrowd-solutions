select c.name, r.rentals_date 
from customers c inner join rentals r 
on c.id = r.id_customers
where r.rentals_date between '20160901' and '20160930';