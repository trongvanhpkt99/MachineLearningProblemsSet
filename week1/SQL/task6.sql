select distinct ID from STATION 
select count(select distinct CITY from STATION)
select count(select CITY from STATION)