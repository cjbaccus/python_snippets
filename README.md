# python_snippets
just small clips of useful python specific snippets of code

# Python

## Snippets

Each section will have a snippet, that may be blocks of code, for specific purposes.

### 1st Snippet 
```python
# below line builds a list with ip addresses ranging from 192.168.1.1 to 192.168.1.254
ips = ["192.168.1.{}".format(str(i)) for i in range(1,255)]
print(ips)
# or use for loop for individuals per line
#for i in ips:
#	print(i)
```


