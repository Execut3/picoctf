## Description
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 22902, but it doesn't speak English...

## Solution

Connect to server:

```bash
$ nc mercury.picoctf.net 22902
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
100 
51 
100 
102 
100 
54 
100 
102 
125 
10 
```


write a python code to decode it:

```python
values = [
    112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 
    116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 
    33, 95, 100, 51, 100, 102, 100, 54, 100, 102, 125, 10
]

# Convert decimal values to ASCII characters
ascii_text = ''.join(chr(val) for val in values)

# Print the ASCII text
print(ascii_text)
```

and run:
```bash
$ python solve.py 
picoCTF{XXXXXXX}
```