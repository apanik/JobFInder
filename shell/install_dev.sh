#!/usr/bin/env bash
sudo apt update
sudo apt install python3 python python-minimal python3-pip python3-dev libmysqlclient-dev -y
pip3 install virtualenv
virtualenv -p python3 venv
