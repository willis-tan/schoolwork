/*
Insert at least 5 tuples
At least 1 restaurant I like
At least 1 restaurant I do not like
At least 1 restaurant as NULL
*/
insert into MyRestaurants values('in-n-out', 'burgers', 2, '2021-03-27', 1);
insert into MyRestaurants values('burger king', 'burgers', 20, '2020-06-01', 0);
insert into MyRestaurants values('subway', 'sandwiches', 10, '2021-03-27', 'NULL');
insert into MyRestaurants values('savoy', 'fusion', 15, '2020-08-10', 1);
insert into MyRestaurants values('baccali', 'hong kong diner', 25, '2021-03-01', 1);
-- handle null values
update MyRestaurants
set rating = NULL
where rating = 'NULL';
