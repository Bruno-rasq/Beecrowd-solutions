select m.id, m.name from movies m inner join genres g on (g.id = m.id_genres) where g.description = 'Action';

/* esssa resposta peguei no forum do beecrowd... um usuario achou um erro de digitação na questão impossibilitando a resposta*/