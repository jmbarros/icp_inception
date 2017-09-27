#!/usr/bin/python 
import os
import os.path
import fileinput
hosts_file="/root/klon/hosts"

#######################################################################
def play_book ( pb, inv ):
  "run playbook"
  book = "ansible-playbook " + pb +  " -i " +  inv
  os.system(book)
  return;

def python ( py ):
  "run py script"
  ps = "/usr/bin/python ./" + py
  os.system(ps)
  return;

def docker_run ( dexec ):
  "run docker"
  ds = "/usr/bin/docker run " + dexec
  os.system(ds)
  return;

def copy ( ori, dest ):
   " coping file "
   pw = "cp " + ori + " " + dest
   os.system(pw)
   return;

##########################################################################
# todo = transform DEF
filein="/etc/ansible/ansible.cfg"
fileout="/etc/ansible/ansible.cfg"

f = open(filein,'r')
filedata = f.read()
f.close()

newdata = filedata.replace("#host_key_checking = False","host_key_checking = False")

f = open(fileout,'w')
f.write(newdata)
f.close()
##########################################################################

docker_run("-e LICENSE=accept -v \"$(pwd)\":/data ibmcom/cfc-installer:2.1.0-beta-1 cp -r cluster /data")
copy("/root/.ssh/id_rsa", "~/klon/cluster/ssh_key")

if os.path.isfile(hosts_file):
  print "Exist"
  play_book("/root/klon/metal/pre_req.yml", "/root/klon/hosts")
  copy("/root/klon/inventory", "/root/klon/cluster/hosts")
  docker_run("-e LICENSE=accept --net=host -t -v \"$(pwd)\"/cluster:/installer/cluster ibmcom/cfc-installer:2.1.0-beta-1 install")
else:
  print "File doesn't exists"
  copy("/root/klon/inventory", "/root/klon/cluster/hosts")
#play_book("~/klon/metal/hosts.yml", "~/klon/hosts")

