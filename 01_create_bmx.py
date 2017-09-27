#!/usr/bin/python 
import os
import os.path
sl_path="/root/.softlayer"

#######################################################################
def play_book ( pb ):
  "run playbook"
  book = "ansible-playbook ./" + pb
  os.system(book)
  return;

def python ( py ):
  "run py script"
  ps = "/usr/bin/python ./" + py
  os.system(ps)
  return;


##########################################################################

if os.path.isfile(sl_path):
  print "Exist"
  play_book("bmx/create_bmx.yml")
  python("bmx/config_bmx.py")
else:
  print "File doesn't exists, please run \"slcli config setup\" "
