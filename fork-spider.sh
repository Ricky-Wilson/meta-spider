#!/bin/bash
# Script to fork instances of meta-spider
# pass -k as an arg to kill all instances of meta-spider

function forkSpiders {
	python ./meta-spider.py $1 >/dev/null &
	if [ "$1" = "-k" ] 
	then
	echo "Killing Spiders"
	pkill -f meta-spider.py
	fi
}

forkSpiders $1
