select
    packages.year,
    sender.name as sender,
    receiver.name as receiver
    
from packages 
inner join users as sender
on packages.id_user_sender = sender.id

inner join users as receiver
on packages.id_user_receiver = receiver.id

where 
(packages.color = 'blue'or packages.year = '2015')
and sender.address != 'taiwan'
and receiver.address != 'taiwan'

order by packages.year desc,
packages.id_package desc;