## Description
This website can be rendered only by picobrowser, go and catch the flag! https://jupiter.challenges.picoctf.org/problem/28921/ (link) or http://jupiter.challenges.picoctf.org:28921

## Solution

```bash
$ curl https://jupiter.challenges.picoctf.org/problem/28921/flag --header "User-Agent: picobrowser" | grep picoCTF

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2115  100  2115    0     0   1640      0  0:00:01  0:00:01 --:--:--  1640
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{XXXXXXX}</code></p>
```