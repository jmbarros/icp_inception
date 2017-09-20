#!/usr/bin/python 
#create inception
### todo
# add check slcli file
#######################################################################
#defs

import os

def yum_install ( pkg ):
   "install via yum"
   install = "yum install -y  " + pkg
   os.system(install)
   return;

def play_book ( pb ):
   "run playbook"
   book = "ansible-playbook ./" + pb
   os.system(book)
   return;

def install_galaxy ( galaxy ):
   "install galaxy repo"
   ig = "ansible-galaxy install " + galaxy
   os.system(ig)
   return;

def git ( url ):
   " using git"
   gt = "git clone " + url
   os.system(gt)
   return;

def copy ( ori, dest ):
   " coping file "
   pw = "cp " + ori + " " + dest
   os.system(pw)
   return;

 ############
yum_install("epel-release")
yum_install( "ansible" )
yum_install( "git" )
git("https://github.com/jmbarros/icp_inception.git")
install_galaxy( "jmbarros.icp" )
play_book( "icp_inception/inception.yml")