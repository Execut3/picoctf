## Description
Can you break into this super secure portal? https://jupiter.challenges.picoctf.org/problem/17682/ (link) or http://jupiter.challenges.picoctf.org:17682

## Solution
We are given a js login page that should find the password to pass it.
here is the given js code:

```javascript
function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == '706c') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_b') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == '5}') {
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
    
  }
```

simply we can find the value using python below:
```python
flag = [' ' for i in range(4*8)]
flag[:4] = 'pico'
flag[4*6:4*7] = '706c'
flag[4:2*4] = 'CTF{'
flag[4*4:4*5] = 'ts_p'
flag[4*3:4*4] = 'lien'
flag[4*5:4*6] = 'lz_b'
flag[4*2:4*3] = 'no_c'
flag[4*7:4*8] = '5}'
print(''.join(flag))
```