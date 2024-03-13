## Description
Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/9670/ (link) or http://jupiter.challenges.picoctf.org:9670


## Solution
We just need to view source codes and css and js files. the flag is 3 parted and located in following file sources:


```
index.html
	<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
```

```
mycss.css
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
```

```
myjs.js
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?2e7b23e3} */
```

```
flag is: picoCTF{XXXXXXX}
```