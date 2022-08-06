#!/bin/bash

# This script takes in a list of IP addresses and uses each entry with Enum4Linux

if [ "$#" != 1 ]
then
	echo "Usage: ./enum4range.sh <IP_list.txt>"
	exit 1
fi	

while read line; do
	enum4linux -a $line
done < $1
