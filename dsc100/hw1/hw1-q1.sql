-- set up the table
create table Edges(
  Source integer,
  Destination integer
);

-- insert tuples
insert into Edges values (10,5);
insert into Edges values (6,25);
insert into Edges values (1,3);
insert into Edges values (4,4);

-- return all tuples
select *
from Edges;

-- return the column Source
select Source
from Edges;

-- return all tuples such that Source > Destination
select *
from Edges
where Source > Destination;

insert into Edges values ('-1', '2000');
/* no errors were produced.
this is due to sqlite3 casting the strings into integers
*/
