select 
    empregados.cpf,
    empregados.enome,
    departamentos.dnome
    
from empregados 
inner join departamentos 
on departamentos.dnumero = empregados.dnumero

where empregados.cpf_supervisor is null
order by empregados.cpf