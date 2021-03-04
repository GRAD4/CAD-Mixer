#!/bin/bash
# This script replaces pyinstaller installed with pip by default with a patched version specifically for pacman distros such as ArchLinux. 
pip remove pyinstaller
wget github.com/bwoodsend/pyinstaller/archive/5540.zip
pip install 5540.zip
rm 5540.zip
