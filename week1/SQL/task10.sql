SELECT DISTINCT city
FROM   station
WHERE  city LIKE '^[aeiouAEIOU].*[aeiouAEIOU]$'