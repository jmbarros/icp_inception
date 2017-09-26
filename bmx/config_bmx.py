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
new_file = "[bluemix] \n"
with open('/etc/ansible/hosts', 'wb') as file_object :
           file_object.write(new_file)

with open('./hosts.ansible', 'wb') as file_object :
           file_object.write("")

with open("./.to_create") as f:
    for line in f:
       vs = (line.rstrip('\n'))	
       ssh = ip (vs)
       key = credentials (vs)
       display = "... collecting data from " + vs + " at " + ssh.rstrip("\n")  
       inventory = ssh.rstrip("\n") + " ansible_user=root ansible_ssh_pass=" + key
       hosts = ssh.rstrip("\n") + " " + vs + "\n"
       print display
       with open('/etc/ansible/hosts', 'a') as file_object :
           file_object.write(inventory)
       with open('./hosts.ansible', 'a') as file_object :
	   file_object.write(hosts)

play="cat ./hosts.ansible >> /etc/hosts\n" + "ansible-playbook conf_bluemix.yml\n"
with open('./install_hosts.sh', 'a') as file_object:
	file_object.write(play)
print "... done !"
print ""
print "Please, execute the command below to create your hosts on your targets:"
print "sh ./install_hosts.sh"
#print "If you want add Bluemix hostnames to this server, execute:"