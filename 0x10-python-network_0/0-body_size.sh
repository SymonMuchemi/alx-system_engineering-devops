#!/bin/bash
# displays the size of the body of the response

if [ $# -ne 1 ]
then
	exit
else
	curl --write-out "%{size_download}\n" -s -o /dev/null "$1"
fi
