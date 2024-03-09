## Description
Can you get the flag? Go to this website and see what you can discover.

## Solution
the webpage provides and login with username password.
which username and password are stored locally in `secret.js` file:

```js



function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}


```

and by login with these username password will get the flag.