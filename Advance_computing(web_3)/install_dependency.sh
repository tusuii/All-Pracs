#!/bin/bash

# Update Packages
sudo apt update && sudo apt upgrade -y

# Install Visual Studio Code
wget "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64" -O vscode.deb
sudo dpkg -i vscode.deb

# Install cURL
sudo apt install curl -y
curl -V

# Install Git
sudo apt install git -y

# Install NVM (Method 1)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
if [ $? -ne 0 ]; then
  # If Method 1 fails, use Method 2
  echo "185.199.108.133 raw.githubusercontent.com" | sudo tee -a /etc/hosts
  source ~/.bashrc
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
fi
# Verify NVM installation
command -v nvm

# Install NodeJS
nvm install --lts
node -v
npm -v

# Install Docker and Docker-Compose
sudo apt install docker-compose -y
sudo usermod -aG docker $USER
docker-compose --version
docker --version

# Install JQ
sudo apt install jq -y
jq --version

# Install Build Essential
sudo apt install build-essential -y
dpkg -l | grep build-essential

# Install Go
curl -OL https://go.dev/dl/go1.21.4.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.21.4.linux-amd64.tar.gz
# Add Go to PATH
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.profile
source ~/.profile
go version

# Install Minifab
curl -o minifab -sL https://tinyurl.com/yxa2q6yr && chmod +x minifab
sudo cp minifab /usr/local/bin
minifab

# Restart System
echo "The system will restart in 10 seconds to apply all changes..."
sleep 10
sudo reboot
