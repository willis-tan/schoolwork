/*
Returns all restaurants that are within and including 10 mins from your house.
*/
select rname
from MyRestaurants
where distance <= 10;
