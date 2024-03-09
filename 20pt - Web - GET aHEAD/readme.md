## Description
Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:47967/

## Solution
as the description told, need to make a HEAD request to server,

```bash
$ curl --head http://mercury.picoctf.net:47967/
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_cca66bd3}
Content-type: text/html; charset=UTF-8

```