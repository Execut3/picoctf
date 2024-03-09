## Description
How about trying to match a regular expression

Additional details will be available after launching your challenge instance.

## Solution
We are given a search box that uses following js:

```js
	function send_request() {
		let val = document.getElementById("name").value;
		// ^p.....F!?
		fetch(`/flag?input=${val}`)
			.then(res => res.text())
			.then(res => {
				const res_json = JSON.parse(res);
				alert(res_json.flag)
				return false;
			})
		return false;
	}
```

We need to provide a value that latches regex: `^p.....F!?`

By submiting this value will get the flag:

```
p12345F!
```