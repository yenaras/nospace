# NoSpace
##### Video Demo: https://www.youtube.com/watch?v=j8HY4FUUE9w
---
##### Description:
Do you use the command line a lot? Are you tired of spaces and/or capitalization 
in your files that you have to waste precious keystrokes to put quotes around or
hold the shift key?
NoSpace might be for you!

I built this script as my final project for Harvard's CS50P, Introduction to 
Programming With Python.

---
### Installation
---
---
```py
pip install nospace
```

---
### Usage
---
Personally, I made the script executable with `chmod +x` and 
moved it to /usr/local/bin/nospace
so I can run it anywhere. Otherwise you have to move it to the directory you want to 
use it in and run it with python(or python3 on Ubuntu, or python or py on Windows).

_example usage_
```py
nospace -p test_directory -c lower -d 1 -o files -s -
```

```py
usage: nospace [-h] [-d DEPTH] [-c {lower,title,upper}] [-o {both,files,folders}] [-s SEPERATOR] [-p PATH]

rename files in bulk to remove spaces

options:
  -h, --help            show this help message and exit
  -d DEPTH, --depth DEPTH
                        maximum depth of folders to traverse
  -c {lower,title,upper}, --case {lower,title,upper}
                        case of the renamed files and folders (lower, title, or upper)
  -o {both,files,folders}, --objects {both,files,folders}
                        objects to process (files, folders, or both)
  -s SEPERATOR, --seperator SEPERATOR
                        separator to replace spaces with (default is _)
  -p PATH, --path PATH  optional file path to start with
```
---
##### LICENSE

---
This repo is licensed under the permissive MIT license.  You can do whatever you want with it.
