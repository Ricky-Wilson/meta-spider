from MySQLdb import *
import MySQLdb
import MySQLdb.cursors
from urlparse import urlparse
from os import mkdir
from os import system
from requests import get
import posixpath

def ext_list():
	ext_list1 = ['.html','.xml','.php','.js','.png','.gif','.asp','css']
	ext_list2 = ['.exe','.pdf','.txt','.py','.pl','.json','.bmp','.svg']
	ext_list3 = ['.swf','.zip','.tar','.gz','.deb','.bin','.egg','.jar']
	ext_list4 = ['.mp3','.mp4','.torrent','.rar','iso','.flack','.ogg','git','.css']
	ext_list = ext_list1 + ext_list2 + ext_list3 + ext_list3 + ext_list4
	return ext_list

def sub_domain_list():
	domain_list1 = ['http://rss.','http://feeds.','http://mail.','http://admin.']
	domain_list2 = ['http://edit.','http://cdn.','http://news.']
	domain_list = domain_list1 + domain_list2
	return domain_list

def key_term_list():
	term_list1 = ['python','science','news','exploits','javascript','rss']
	term_list2 = ['feeds','json','data','scripts','css']
	term_list = term_list1 + term_list2
	return term_list

def getFileName(url):
	url = url.split("http://")
	filename = posixpath.basename(url[0])
	return filename
	
# Connection to the database
db = MySQLdb.connect( host="localhost", 
											port=3306, user="root", 
											passwd="thedoors0", 
											db="meta-spider",
											cursorclass=MySQLdb.cursors.DictCursor)
"""\
	In computer science, a database cursor is a control structure 	
	that enables traversal over the records in a database. 
	Cursors facilitate subsequent processing in conjunction with the traversal, 
	such as retrieval, addition and removal of database records
"""

cursor = db.cursor()

def makedirs():
	dirs = [
					'data',
					'data/images',
					'data/xml',
					'data/binary',
					'data/javascript'
					]
	for dir in dirs:
		try:		
			mkdir(dir)
		except OSError:
			pass
makedirs()
	

def sqlmap(options):
	system(str("sqlmap/sqlmap.py %s" % (options)))

#sqlmap("-u http://www.cideko.com/pro_con.php?id=3")

def links():
	cursor.execute("SELECT  `link` FROM  `data` LIMIT 0 , 1000000")
	links = cursor.fetchall()
	return links

def files():
	for link in links():
		files = []
		filename = getFileName(link['link'])
		for ext in ext_list():
			if len(filename) > 1:
				if filename.endswith(ext):
					files.append(filename)
		for file in files:
			print file

def file_ext(link):
	filename = getFileName(link)
	for ext in ext_list():
		if len(filename) > 1:
			if filename.endswith(ext):
				print filename

files()

def sites():
	sites = []
	for link in links():
		parsedLink = urlparse(link['link'])   
		hostname = parsedLink.hostname
		if hostname not in sites:
			sites.append(hostname)
	return sites

def titles():
	unique = []
	cursor.execute("SELECT  `title` FROM  `data` LIMIT 0 , 1000000")
	titles = cursor.fetchall()
	for u in titles:
		if u not in unique:
			unique.append(u['title'])
	return titles

def images():
	images = []
	for link in links():
		if link['link'].endswith(".png"):
			images.append(link['link'])
		if link['link'].endswith("jpg"):
			images.append(link['link'])
		if link['link'].endswith("gif"):
			images.append(link['link'])
	return images

def feeds():
	feeds = []
	for link in links():
		if link['link'].endswith(".xml"):
			feeds.append(link['link'])
		if link['link'].endswith("/feeds"):
			feeds.append(link['link'])
		if link['link'].endswith("/feed"):
			feeds.append(link['link'])
		if link['link'].endswith("rss"):
			feeds.append(link['link'])
		if link['link'].endswith("/rss/"):
			feeds.append(link['link'])
		if link['link'].startswith("http://rss."):
			feeds.append(link['link'])
		if link['link'].startswith("http://feeds."):
			feeds.append(link['link'])
	return feeds

def xml():
	xml_files = []
	for link in links():
		if getFileName(link['link']).endswith(".xml"):
			if link['link'] not in xml_files:
				xml_files.append(link['link'])
	for link in xml_files:
		filename = getFileName(link)
		content = get(link).content
		path = "data/xml/%s" %(filename)
		print path
		file = open(path,"w").write(content)

def gov_links():
	gov_links = []
	for link in links():
		if link['link'].endswith(".gov"):
			if link['link'] not in gov_links:
				gov_links.append(link['link'])
		if link['link'].endswith(".mil"):
			if link['link'] not in gov_links:
				gov_links.append(link['link'])
	return gov_links 

def binary():
	binary = []
	for link in links():
		if link['link'].endswith(".exe"):
			binary.append(link['link'])
	return binary


def sitemaps():
	sitemaps = []
	for link in links():
		if "sitemap" in link['link']:
			if link['link'] not in sitemaps:
				sitemaps.append(link['link'])
	return sitemaps

def javascript():
	javascript_files = []
	for link in links():
		if getFileName(link['link']).endswith("js"):
			if link['link'] not in javascript_files:
				javascript_files.append(link['link'])
	for link in javascript_files:
		filename = getFileName(link)
		content = get(link).content
		path = "data/javascript/%s" %(filename)
		print path
		file = open(path,"w").write(content)

def downloadFile(link):
	filename = getFileName(link)
	content = get(link).content
	path = "data/javascript/%s" %(filename)
	print path
	file = open(path,"w").write(content)

def php():
	php = []
	for link in links():
		if ".php?" in link['link']:
			if link['link'] not in php:
				php.append(link['link'])
	return php

def sqlCheck():
	empty = open("sqlmap_list","w").write(" ")
	sqlmap_list = open("sqlmap_list","a")
	sql_mapable = []
	for link in links():
		if "id=" in link['link']:
			if link['link'] not in sql_mapable:
				sql_mapable.append(link['link'])
				sqlmap_list.write(link['link']+"\n")
	return sql_mapable

def asp():
	asp = []
	for link in links():
		if link['link'].endswith(".asp"):
			if link['link'] not in asp:
				asp.append(link['link'])
	return asp

def zip():
	zip = []
	for link in links():
		if link['link'].endswith(".zip"):
			if link['link'] not in zip:
				zip.append(link['link'])
	return zip

def text():
	text = []
	for link in links():
		if link['link'].endswith(".txt"):
			if link['link'] not in text:
				text.append(link['link'])
	return text

def cgi():
	cgi = []
	for link in links():
		if link['link'] not in cgi:
			if "/cgi-bin/" in link['link']:
				cgi.append(link['link'])
	return cgi
	
def initTables():

	sql = """\
				CREATE TABLE data(	Id INT PRIMARY KEY AUTO_INCREMENT, 
					link VARCHAR(1000000), 
					keywords VARCHAR(1000000), 
					title VARCHAR(100000) )
				"""
	cursor.execute(sql)
	try:	
		cursor.execute("""\
										CREATE TABLE feeds(Id INT PRIMARY KEY AUTO_INCREMENT, 
										feeds VARCHAR(1000000)) 
									""")
	except:pass

def insert(link,keywords,title):
	sql = """\
				INSERT INTO data(link,keywords,title)VALUES("%s","%s","%s")
				""" % (link,keywords,title)

	# Commit your changes in the database

	try:
		# Execute the SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		db.commit()
	except:
		# Rollback in case there is any error
		db.rollback()
	
