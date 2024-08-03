# python_snippets
just small clips of useful python specific snippets of code

# Python

## Snippets

Each section will have a snippet, that may be blocks of code, for specific purposes.
* These scripts will be able to be copied from the github readme page and pasted directly where you need them.
* These copied snippets can be tested by instantiating the python interpreter on your local CLI and pasting the snippet in the interpreter.
### Example python interpreter

```bash
python

```

```
# python
Python 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>># to exit remember type exit()
>>>exit()
#

```
```bash
exit()

```

### 1st Snippet 
```python
# below line builds a list with ip addresses ranging from 192.168.1.1 to 192.168.1.254
# ips = ["192.168.1.{}".format(str(i)) for i in range(1,255)]
# This specific snippet is for GNS3 or network lab work where each consecutive device 
# gets a loopback0 IP of 1.1.1.1, 2.2.2.2 depending on number of switch

ips = [f"{i}.{i}.{i}.{i}" for i in range(1,7)]
print(ips)
# or use for loop for individuals per line
#for i in ips:
#	print(i)


```
#### 1st Snippet (one liner)
```bash
python -c 'ips = [f"{i}.{i}.{i}.{i}" for i in range(1, 7)]; [print(ip) for ip in ips]' > ipaddresses101.txt



```
### 2nd Snippet
```python
#write a comment style line out with a couple of variables for name  and IP
HST = "host1"
IP = "192.168.1.1"
print("!"*50 + f"Host: {HST} IP: {IP}" + "!"*50)

```

### 3rd Snippet
```python
#If combined with Snippet 1 this will write a flat text file with ip addresses in it from ips
#otherwise it will just write out ips from variable below
#(try,except, else checks to see if ips is empty)

try:
    ips
except NameError:
    ips = ["1.1.1.1","2.2.2.2"]
else:
    print("ips are populated from snippet 1")

with open("ipaddresses1.txt", "w", encoding="utf-8") as invt:
  for ip in ips:
	  invt.write(ip+"\n")

print("File ipaddresses1.txt has been written!")

#This should result in a file written in directory you are in with an ip per line

```
### 4th Snippet
```python
# This will write out an ansible inventory file with IPS 
# that were created with snippet 3 or just a flat iP file
# This script is included in repo as inventory_ansible.py and
# is best executed as python inventory_ansible.py
# the interpreter doesn't work well for just copying and pasting


import glob

ipfile = glob.glob("*ipaddress*")
#if else for if file exists or not
if ipfile:
    with open(ipfile[0], "r", encoding="utf-8") as FH:
        ipadds = []

        for line in FH.readlines():
          ipadds.append(line.strip())

        GROUP_NAME = "sw"
        inventory = f"[{GROUP_NAME}]\n"
        for index, ip in enumerate(ipadds, start=1):
            inventory += f"host_{index} ansible_host=\"{ip}\"\n"

        with open("hosts", "w") as hosts_file:
            hosts_file.write(inventory)

        print("OK inventory file written!!")
else:
    print("No ipaddresses file found exiting now!")

```
### 5th Snippet

```python
# This script will execute another python file from within a python script or interpreter

with open('inventory_ansible.py') as file:
  exec(file.read())

# You can copy and rename 'inventory_ansible.py' with whatever python script you need to execute

```

#### 5th Snippet (one-liner)
```bash
python -c "with open('inventory_ansible.py') as file: exec(file.read())"


```

```mermaid
  info
```
