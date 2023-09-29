(
    select city_name, population
    from cities
    where cities.id = 2
)

UNION ALL

(
   select city_name, population
    from cities
    where cities.id = 11
)