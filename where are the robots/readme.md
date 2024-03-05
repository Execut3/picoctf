## Description
Can you find the robots? https://jupiter.challenges.picoctf.org/problem/56830/ (link) or http://jupiter.challenges.picoctf.org:56830


## Solution
checking `robots.txt` file, gives us:

```html
User-agent: *
Disallow: /1bb4c.html
```

and checking the location given:
```html
Guess you found the robots
picoCTF{ca1cu1at1ng_Mach1n3s_1bb4c}
```