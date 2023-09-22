select cand.name, 
ROUND(avg(((s.math * 2) + (s.specific * 3) + (s.project_plan * 5))/10))
from candidate cand inner join score s
on s.candidate_id =  cand.id
group by cand.name
order by ROUND desc
