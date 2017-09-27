#!/usr/bin/bash
cd /root/klon//cluster
/usr/bin/docker run -e LICENSE=accept --net=host -t -v "$(pwd)":/installer/cluster ibmcom/cfc-installer:2.1.0-beta-1 install
