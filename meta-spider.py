import sys
import re
import urllib2
import urlparse
from time import sleep 
from os import system
from database import initTables, insert
from database import links as LINKS
from database import getFileName
from database import ext_list
from database import sub_domain_list
from database import key_term_list

# Connect to the database and create the tables
def install():
	try:
		initTables()
	except:
		pass
install()

def main():
	# The Seed
	tocrawl = set([sys.argv[1]])	
	crawled = set([])

	# Pull keywords from HTML meta tags
	keywordregex = re.compile('<meta\sname=["\']keywords["\']\scontent=["\'](.*?)["\']\s/>')
	linkregex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')

	while len(tocrawl) >=1:
		try:
			crawling = tocrawl.pop()
			system("clear")
			filename = getFileName(crawling)
			print "Crawling --> %s \n"% (crawling)
			print "Crawled --> %s \n" % (len(crawled))
			print "Left to crawl --> %s \n" % (len(tocrawl))
			#print "Links in database  --> %s \n" % (len(LINKS())))
		except KeyError: 
			#raise StopIteration
			continue
		url = urlparse.urlparse(crawling)

		try:
			# Download 
			response = urllib2.urlopen(crawling,timeout=500)
		except:
			response = open("tmp","w")
			response = open("tmp","r")
			print "Error crawling: --> %s\n" % (crawling)
			continue
		try:
			msg = response.read()
		except:
			msg = "none"

		# Scrape title
		def title():
			startPos = msg.find('<title>')
			if startPos != -1:
				endPos = msg.find('</title>', startPos+7)
				if endPos != -1:
					title = msg[startPos+7:endPos]
					return title
				else: return "No Title"

		# Scrape keywords
		def keywords():
			keywordlist = keywordregex.findall(msg)
			if keywordlist >=1:
				# Return a string of keywords
				return ",".join(keywordlist)
			else:
				return "none"
		#-- Done Scraping keywords --#

		# Scrape the links
		links = linkregex.findall(msg)
		# Commit all the data to the database
		if crawling not in LINKS():
			print "Adding --> %s to the database\n" % (crawling)
			insert(crawling,keywords(),title())
		else: print "%s all ready in database\n" % (crawling)
		crawled.add(crawling)

		for link in (links.pop(0) for _ in xrange(len(links))):
			if link.startswith('/'):
				link = 'http://' + url[1] + link
			elif link.startswith('#'):
				link = 'http://' + url[1] + url[2] + link
			elif not link.startswith('http'):
				link = 'http://' + url[1] + '/' + link
			if link not in crawled:
				for ext in ext_list():
					if link.endswith(ext):
						tocrawl.add(link)
				
				for subd in sub_domain_list():
					if link.startswith(subd):
						tocrawl.add(link)
				
				for term in key_term_list():
					if term in link:
						tocrawl.add(link)
		#-- Done scraping links --#

try:
	main()
except:
	quit()
