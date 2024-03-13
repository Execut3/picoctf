## Description
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: Addadshashanammu.zip

## Solution

Open the given zip file and grep on all strings to find anything usefull:

```bash
$ unzip Addadshashanammu.zip
$ cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
$ strings fang-of-haynekhtnamet | grep picoCTF
*ZAP!* picoCTF{XXXXXXX}
```