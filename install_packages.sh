#!/bin/bash
#
# Auto-generated apt installation script
# Generated from: apt_history.txt
#
# This script will install all packages from the apt history
#

# Exit on error
set -e

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script with sudo"
    exit 1
fi

echo "Starting package installation..."
echo "====================================="

echo "Running apt update before command 1..."
apt update

echo "Running apt upgrade before command 1..."
apt upgrade -y

echo "Executing command 1: apt install coreutils-from-gnu coreutils-from-uutils- --allow-remove-essential"
apt install -y coreutils-from-gnu coreutils-from-uutils- --allow-remove-essential

echo "Running apt update before command 2..."
apt update

echo "Running apt upgrade before command 2..."
apt upgrade -y

echo "Executing command 2: apt install inxi"
apt install -y inxi

echo "Running apt update before command 3..."
apt update

echo "Running apt upgrade before command 3..."
apt upgrade -y

echo "Executing command 3: apt install build-essential"
apt install -y build-essential

echo "Running apt update before command 4..."
apt update

echo "Running apt upgrade before command 4..."
apt upgrade -y

echo "Executing command 4: apt install pkg-config"
apt install -y pkg-config

echo "Running apt update before command 5..."
apt update

echo "Running apt upgrade before command 5..."
apt upgrade -y

echo "Executing command 5: apt install curl"
apt install -y curl

echo "Running apt update before command 6..."
apt update

echo "Running apt upgrade before command 6..."
apt upgrade -y

echo "Executing command 6: apt install gfortran"
apt install -y gfortran

echo "Running apt update before command 7..."
apt update

echo "Running apt upgrade before command 7..."
apt upgrade -y

echo "Executing command 7: apt install libcfitsio-dev libssl-dev python3-dev"
apt install -y libcfitsio-dev libssl-dev python3-dev

echo "Running apt update before command 8..."
apt update

echo "Running apt upgrade before command 8..."
apt upgrade -y

echo "Executing command 8: apt install libgtk2.0-dev"
apt install -y libgtk2.0-dev

echo "Running apt update before command 9..."
apt update

echo "Running apt upgrade before command 9..."
apt upgrade -y

echo "Executing command 9: apt install texlive-luatex texlive-latex-base texlive-latex-recommended texlive-fonts-recommended"
apt install -y texlive-luatex texlive-latex-base texlive-latex-recommended texlive-fonts-recommended

echo "Running apt update before command 10..."
apt update

echo "Running apt upgrade before command 10..."
apt upgrade -y

echo "Executing command 10: apt install texlive-full"
apt install -y texlive-full

echo "Executing command 11: apt upgrade"
apt upgrade -y

echo "Running apt update before command 12..."
apt update

echo "Executing command 12: apt install git-all"
apt install -y git-all

echo "Running apt update before command 13..."
apt update

echo "Running apt upgrade before command 13..."
apt upgrade -y

echo "Executing command 13: apt install akregator"
apt install -y akregator

echo "====================================="
echo "All packages installed successfully!"
