## Description
Help us test the form by submiting the username as test and password as test! The website running here.

## Solution
We are given a login page with username password `test:test!`
after login we see there is a redirect (using burpsuite to capture the redirect)

this is the redirect value:
```html
<p>Found. Redirecting to <a href="/next-page/id=cGljb0NURntwcm94aWVzX2Fs">/next-page/id=cGljb0NURntwcm94aWVzX2Fs</a></p>
```

and when visiting the redirected page, also again will do a redirect with following data in it:
```html
<!DOCTYPE html>
<head>
    <title>flag</title>
</head>
<body>
    <script>
        setTimeout(function () {
           // after 2 seconds
           window.location = "/next-page/id=bF90aGVfd2F5XzNkOWUzNjk3fQ==";
        }, 0.5)
      </script>
    <p></p>
</body>
```

by decoding these two base64 encoded values and concating them together will get the flag.

```bash
echo 'cGljb0NURntwcm94aWVzX2FsbF90aGVfd2F5XzNkOWUzNjk3fQ==' |base64 --decode
picoCTF{XXXXXXX}
```