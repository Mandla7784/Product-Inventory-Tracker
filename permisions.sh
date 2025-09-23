#!/bin/bash

echo "Fixing Docker permissions..."

if groups $USER | grep -q '\bdocker\b'; then
    echo "User is already in the docker group. Continuing..."
else
    sudo usermod -aG docker $USER
    echo "You have been added to the docker group. Please log out and back in before continuing."
    exit 1
fi


# restarting 
sudo systemctl restart docker


# Build and run
docker build -t product-inventory .
docker run -it product-inventory
