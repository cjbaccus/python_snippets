#!/usr/bin/env python


# below line builds a list with ip addresses ranging from 192.168.1.1 to 192.168.1.254
ips = ["192.168.1.{}".format(str(i)) for i in range(1,255)]
print(ips)
# or use for loop for individuals per line
#for i in ips:
#	print(i)



#write a comment style line out with a couple of variables for name  and IP
hst = "host1"
ip = "192.168.1.1"
print("!"*50 + "Host: {} IP: {}".format(hst,ip) + "!"*50)

#If combined with Snippet 1 this will write a flat text file with ip addresses in it from ips
#otherwise it will just write out ips from variable below
#(try,except, else checks to see if ips is empty)

try:
  ips
except NameError:
  ips = ["1.1.1.1","2.2.2.2"]
else:
  print("ips are populated from snippet 1")

with open("ipaddresses1.txt", "w") as invt:
  for ip in ips:
	  invt.write(ip+"\n")

print("File ipaddresses1.txt has been written!")

#This should result in a file written in directory you are in with an ip per line

with open('inventory_ansible.py') as file:
    exec(file.read())

