#!/bin/bash
#installing require package

pkg update && pkg upgrade -y
clear
echo ''
echo -e "\e[1;32m[+] Installing require package...\e[0m"
sleep 3
pkg install python -y
clear
pkg install python2 -y
clear
pkg install php -y
clear
pkg install json -y
clear
pkg install openssh -y
clear
pkg install wget -y
clear
pkg install bash -y
clear
pip install requests
clear
pip2 install requests
clear
pip install googlesearch
clear
pip2 install googlesearch
clear
echo "[✓] Install bahan selesai"
sleep 1
echo -e "\e[1;32mKetik python santet.py untuk memulai\e[0m"

