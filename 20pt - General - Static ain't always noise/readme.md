## Description
Can you look at the data in this binary: static? This BASH script might help!

## Solution
run the script and input `statis` file in it. it's a simple script to do objdump operation on a file and give some info about code and text sections of binary.

```bash
$ chmod +x ltdis.sh
$ ./ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```

A file `static.ltdis.strings.txt` is created which holds the flag value in it.