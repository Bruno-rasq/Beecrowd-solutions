select 
    records.temperature,
    count(records.mark) as number_of_records
from records

group by records.mark, records.temperature 
order by records.mark;