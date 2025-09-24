#!/bin/bash

echo "Fixing Docker permissions..."
echo "Checking operating system..."

OS="$(uname -s)"

if [[ "$OS" == "Linux"]]; then 
    echo "Linux detected. Fixing Docker permissions..."


    if groups $USER | grep -q '\bdocker\b'; then
        echo "User is already in the docker group. Continuing..."
    else
        sudo usermod -aG docker $USER
        echo "You have been added to the docker group. Please log out and back in before continuing."
        exit 1
    fi


    # restarting 
    sudo systemctl restart docker


    # Check and load veth kernel module
    lsmod | grep veth || sudo modprobe veth

    # Check Docker status
    sudo systemctl status docker

    echo "If you still see errors, consider reinstalling Docker or rebooting your system."


    # Build and run
    echo "buidling....."

    docker build -t product-inventory .
    docker run -it product-inventory

    echo "build successfully.."
