SELECT distinct CITY
 from STATION 
WHERE  lower(substr(city,length(city),length(city))) in('a','e','i','o','u')