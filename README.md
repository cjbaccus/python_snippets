# python_snippets
just small clips of useful python specific snippets of code

# Python

## Snippets

Each section will have a snippet, that may be blocks of code, for specific purposes.
* These scripts will be able to be copied from the github readme page and pasted directly where you need them.
* These copied snippets can be tested by instantiating the python interpreter on your local CLI and pasting the snippet in the interpreter.
### Example python interpreter
```bash
# python
Python 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### 1st Snippet 
```python
# below line builds a list with ip addresses ranging from 192.168.1.1 to 192.168.1.254
ips = ["192.168.1.{}".format(str(i)) for i in range(1,255)]
print(ips)
# or use for loop for individuals per line
#for i in ips:
#	print(i)


```


