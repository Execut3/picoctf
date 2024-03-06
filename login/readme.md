## Description
My dog-sitter's brother made this website but I can't get in; can you help? login.mars.picoctf.net

## Solution
We are given a login page to provide username and password with following js logic:

```javascript
(async () => {
    await new Promise((e => window.addEventListener("load", e))), document.querySelector("form").addEventListener("submit", (e => {
        e.preventDefault();
        const r = {
                u: "input[name=username]",
                p: "input[name=password]"
            },
            t = {};
        for (const e in r) t[e] = btoa(document.querySelector(r[e]).value).replace(/=/g, "");
        return "YWRtaW4" !== t.u ? alert("Incorrect Username") : "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ" !== t.p ? alert("Incorrect Password") : void alert(`Correct Password! Your flag is ${atob(t.p)}.`)
    }))
})();
```

the value `cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ` seem to be the password.
But the code `btoa(document.querySelector(r[e]).value).replace(/=/g, "")` will try to remove any `=` in base64 value of password to '' string.

So if we put == at the end of this value and try to base64 decode it, will get the flag:

```bash
$ echo 'cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ==' |base64 --decode
picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}  
```
