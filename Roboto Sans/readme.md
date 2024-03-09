## Description
The flag is somewhere on this web application not necessarily on the website. Find it. Check this out.

## Solution
As the title hints us,checking `robots.txt`:

```
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```


Base64 decoding:

```
flag1.txt;js/myfi
js/myfile.txt
```

and check location `js/myfile.txt` will get the flag.