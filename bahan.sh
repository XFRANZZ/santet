#!/bin/bash
#installing require package

pkg update && pkg upgrade -y
clear
printf "[+] Installing require package...\n"
sleep 2
pkg install python -y
clear
pkg install python2 -y
clear
pkg install php -y
clear
pkg install json -y
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
printf "Install bahan selesai"
sleep 1
printf "Ketik python santet.py untuk memulai"
 
