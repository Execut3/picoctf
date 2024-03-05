## Description
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? https://jupiter.challenges.picoctf.org/problem/44573/ (link) or http://jupiter.challenges.picoctf.org:44573


## Solution
checking the site, we see a login page, simply login for example with username, password `admin`.

viewing site we see nothing usefull, but checking cookies, see that there is a cookie name admin with value = `False`. just change it to `True`, refresh webpage and you will see the flag.

