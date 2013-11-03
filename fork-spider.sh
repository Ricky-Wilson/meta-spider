

function forkSpiders {
	echo "Starting $0"
	python ./meta-spider.py $1 >/dev/null &
	if [ "$1" = "-k" ] 
	then
	echo "Killing Spiders"
	pkill -f meta-spider.py
	fi
}

forkSpiders $1
