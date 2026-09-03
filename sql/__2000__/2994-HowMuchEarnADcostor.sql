select d.name,
    round(sum((att.hours * 150)+((att.hours * 150)* ws.bonus) / 100),1) as salary
    
    from doctors d inner join attendances att
    on att.id_doctor = d.id inner join work_shifts ws
    on ws.id = att.id_work_shift
    
    group by d.name
    order by salary desc;