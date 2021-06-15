#!/bin/bash

version=$(python -V 2>&1 | grep -Po '(?<=Python )(.+)')
if [[ -z "$version" ]]
then
    echo "ERROR: Python is NOT installed."
else
	echo "Python is installed."
	python3 myfortune.py | lolcat
fi
