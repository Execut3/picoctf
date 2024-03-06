## Description
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

## Solution
It seem to be a base64 encoded strings. decode it:

```bash
$ echo 'bDNhcm5fdGgzX3IwcDM1' | base64 --decode
l3arn_th3_r0p35
```