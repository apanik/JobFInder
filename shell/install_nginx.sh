#!/bin/bash
# Install nginx
sudo apt install nginx
# Copy nginx.conf file to nginx folder
sudo cp /var/p7/shell/nginx.conf /etc/nginx
# Restart Nginx
sudo service nginx restart

