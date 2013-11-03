from urlparse import urlparse
import re

def feeds(urls):
	parsed = []
	sorted = []
		

def netlocs(list):
	parsed = []
	sorted = []
	for url in list:
		try:
			parsed.append(urlparse(url).netloc)
		except ValueError:
			continue
	for x in parsed:
		if x not in sorted:
			sorted.append(x)
	return sorted

nets = netlocs(open("links.txt","r").readlines())

#erase file
open("sites.txt","w")

for net in nets:
	print net
	open("sites.txt","a").write(net + "\n")
