#!/usr/bin/python 
#######################################################################
import os
import subprocess
##############
def credentials ( vs ):
   "get password"
   output = subprocess.check_output("slcli vs credentials " + vs + "|grep root | awk '{print $2}'", shell=True)
   return (output);

def ip ( vs ):
    "get IP"
    output = subprocess.check_output("slcli vs detail " + vs + "|grep public_ip |awk '{print $2}'", shell=True)
    return (output);

###############
with open('/root/klon/hosts', 'wb') as file_object :
           file_object.write("")

master01=ip("master01")
worker01=ip("worker01")
proxy01=ip("proxy01")

with open("/root/klon/inventory", 'wb') as file_object :
           file_object.write("[master]")
with open('/root/klon/inventory', 'a') as file_object :
           file_object.write(master01)
with open('/root/klon/inventory', 'a') as file_object :
           file_object.write("[worker]")
with open('/root/klon/inventory', 'a') as file_object :
           file_object.write(worker01)
with open('/root/klon/inventory', 'a') as file_object :
           file_object.write("[proxy]")
with open('/root/klon/inventory', 'a') as file_object :
           file_object.write(proxy01)

with open("/root/klon/bmx/to_create.txt") as f:
    for line in f:
       vs = (line.rstrip('\n'))	
       ssh = ip (vs)
       key = credentials (vs)
       display = "... collecting data from " + vs + " at " + ssh.rstrip("\n")  
       inventory = ssh.rstrip("\n") + " ansible_user=root ansible_ssh_pass=" + key
       hosts = ssh.rstrip("\n") + " " + vs + "\n"
       print display
       with open('/root/klon/hosts', 'a') as file_object :
           file_object.write(inventory)



print "... done !"
print ""
