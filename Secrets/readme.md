## Description
We have several pages hidden. Can you find the one with the flag? The website is running here.

## Solution
Easy challenge. to solve just check source codes and look on places found in source.

In index.html source, hint on /secret/ path
Checking it:

```html
<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <link rel="stylesheet" href="hidden/file.css" />
  </head>

  <body>
    <h1>Finally. You almost found me. you are doing well</h1>
    <img src="https://media1.tenor.com/images/0a6aff9f825af62c05adfbd75039cc7b/tenor.gif?itemid=4648337" alt="Something Like That GIF - Andy Parksandrecreation Wtf GIFs" style="max-width: 833px; background-color: rgb(151, 121, 85);" width="833" height="937.125">
  </body>
</html>
```

Now check `secret/hidden/`
```html
<!DOCTYPE html>
<html>
  <head>
    <title>LOGIN</title>
    <!-- css -->
    <link href="superhidden/login.css" rel="stylesheet" />
  </head>
  <body>
  ....
  ..

```
and going to `superhidden`:
```html
<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <link rel="stylesheet" href="mycss.css" />
  </head>

  <body>
    <h1>Finally. You found me. But can you see me</h1>
    <h3 class="flag">picoCTF{succ3ss_@h3n1c@10n_790d2615}</h3>
  </body>
</html>

```