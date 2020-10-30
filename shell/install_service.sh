#!/bin/bash
# Copy project.service unit file to system folder
sudo cp /var/p7/shell/p7.service /etc/systemd/system/
# Load ALL system unit files into memory
sudo systemctl daemon-reload
# Make the service start during boot [without extension enable]
sudo systemctl enable p7
# Start the service manually
# sudo systemctl start projectseven or, sudo service projectseven start
# Stop the service manually
# sudo systemctl stop projectseven or, sudo service projectseven stop
