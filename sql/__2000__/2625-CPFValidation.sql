select 
    regex_replace(np.cpf, '(\d{3})(\d{3})(\d{3})(\d{2})', '\1.\2.\3-\4')
    
from customers c inner join natural_person np
on np.id_customers = c.id;