#!/usr/bin/env python

import glob

ipfile = glob.glob("*ipaddress*")
#if else for if file exists or not
if ipfile:
    with open(ipfile[0], "r") as FH:
        ipadds = []

        for line in FH.readlines():
          ipadds.append(line.strip())

        group_name = "sw"
        inventory = f"[{group_name}]\n"
        for index, ip in enumerate(ipadds, start=1):
            inventory += f"host_{index} ansible_host=\"{ip}\"\n"

        with open("hosts", "w") as hosts_file:
            hosts_file.write(inventory)

        print("OK inventory file written!!")
else:
    print("No ipaddresses file found exiting now!")


