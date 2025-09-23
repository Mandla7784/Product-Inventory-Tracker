#!/bin/bash 

echo "fixing permision for docker..."

sudo usermod -aG docker $USER

newgrp docker