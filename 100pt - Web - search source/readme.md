## Description
The developer of this website mistakenly left an important artifact in the website source, can you find it? The website is here

## Solution
as the description is telling us, the flag is somewhere is source files.
we download all files using `wget` command recursively


```bash
 wget -r http://saturn.picoctf.net:65086
```

and search for `picoCTF` value in all files using below command:
```bash
$ grep -r 'picoCTF' .
./saturn.picoctf.net:65086/css/style.css:/** banner_main picoCTF{XXXXXXX} **/ wget -r http://saturn.picoctf.net:65086
```
and the flag is in style.css file.