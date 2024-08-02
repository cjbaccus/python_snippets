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
>>># to exit remember type exit()
>>>exit()
#

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

### 2nd Snippet
```python
#write a comment style line out with a couple of variables for name  and IP
hst = "host1"
ip = "192.168.1.1"
print("!"*50 + "Host: {} IP: {}".format(hst,ip) + "!"*50)

```

### 3rd Snippet
```python
#If combined with Snippet 1 this will write a flat text file with ip addresses in it from ips
#otherwise it will just write out ips from variable below (if else checks to see if ips is empty
if not ips:
	ips["1.1.1.1","192.168.1.1", "10.10.10.10","8.8.8.8"]
else:

with open("ipaddresses1.txt", "w") as invt:
  for ip in ips:
	  invt.write(ip+"\n")

#This should result in a file written in directory you are in with an ip per line

