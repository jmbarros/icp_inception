#!/usr/bin/bash
cd ~ 
/usr/bin/docker run -e LICENSE=accept -v "$(pwd)":/data ibmcom/cfc-installer:2.1.0-beta-1 cp -r cluster /data
cat ~/.ssh/id_rsa > ~/cluster/ssh_key
echo "" > ~/cluster/hosts
/usr/bin/ansible-playbook ~/icp_inception/hosts.yml -i ~/icp_inception/inventory
cd ~/cluster
/usr/bin/docker run -e LICENSE=accept --net=host -t -v "$(pwd)":/installer/cluster ibmcom/cfc-installer:2.1.0-beta-1 install