/*
Returns all restaurants that you like, but have not visited since more than 3 
months ago.
*/
select rname
from MyRestaurants
where last_vist > (select date('now', '-3 month'));
