
function find_xml {
 cat links.txt | sort -u |  awk '/.xml*$/'
}

function find_javascript {
 cat links.txt | sort -u |  awk '/.js*$/'
}

find_javascript
