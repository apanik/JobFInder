#!/usr/bin/env bash

############################################################
################ P R E R E Q U I S I T E S #################
############################################################
# Getting the source code:
#
# cd /var/
# sudo mkdir p7
# sudo chown ubuntu p7
# git clone https://github.com/Ishraak-Solutions/jobxprss-web.git p7
#python3 -m venv venv
############################################################

sudo apt update
sudo apt install python3 python python-minimal python3-pip python3-dev libmysqlclient-dev -y
pip3 install virtualenv
cd /var/
sudo mkdir p7_static
sudo chown ubuntu p7_static
cd p7
git checkout master
virtualenv -p python3 venv
