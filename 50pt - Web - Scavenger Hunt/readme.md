## Description
There is some interesting information hidden around this site http://mercury.picoctf.net:39491/. Can you find it?

## Solution

again we should check part of source codes and some places for flag.

```
view-source:http://mercury.picoctf.net:39491/
	<!-- Here's the first part of the flag: picoCTF{t -->
```

```
view-source:http://mercury.picoctf.net:39491/mycss.css
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

```
view-source:http://mercury.picoctf.net:39491/robots.txt
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

the `robots.txt` file hints on checking `.htaccess` file:
```
view-source:http://mercury.picoctf.net:39491/.htaccess
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

the previous `robots.txt` file, hinted it is mac os. Mac creates a default file in each folder named `.DS_Store`
```
view-source:http://mercury.picoctf.net:39491/.DS_Store
Congrats! You completed the scavenger hunt. Part 5: _f7ce8828}
```


```
flag: picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_f7ce8828}
```

