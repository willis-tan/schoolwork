-- headers are off
--csv format
.mode csv
SELECT * FROM MyRestaurants;

-- list form, delimited by "|"
.mode list
SELECT * FROM MyRestaurants;

-- column form, with column width of 15
.mode column
.width 15
SELECT * FROM MyRestaurants;

-- This time with headers on
.headers on

--csv format
.mode csv
SELECT * FROM MyRestaurants;

-- list form, delimited by "|"
.mode list
SELECT * FROM MyRestaurants;

-- column form, with column width of 15
.mode column
.width 15
SELECT * FROM MyRestaurants;
