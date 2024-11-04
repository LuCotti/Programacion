#!/bin/bash

sudo fdisk /dev/sdc << EOF
n
p


+2G
w
EOF
lsblk -f /dev/sdc
echo "Listo perri"
