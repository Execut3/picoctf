## Description
Connect to this PostgreSQL server and find the flag! psql -h saturn.picoctf.net -p 54665 -U postgres pico Password is postgres

## Solution
We are given a postgresql connection:

```bash
$ psql -h saturn.picoctf.net -p 54665 -U postgres pico
```

and checking database:
```bash
pico=# \l
\                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privi
leges   
-----------+----------+----------+------------+------------+------------+-----------------+---------------
--------
 pico      | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres   
       +
           |          |          |            |            |            |                 | postgres=CTc/p
ostgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres   
       +
           |          |          |            |            |            |                 | postgres=CTc/p
ostgres
(4 rows)

pico=# \d
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)

pico=# select * from flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)

```