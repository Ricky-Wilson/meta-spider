#!/usr/bin/python2.7
import socket
from time import ctime 
from time import sleep
from re import *
import zlib
import re
from database import initTables, insert
from database import links as LINKS
from database import sites
from database import getFileName

def log(fname,entry):
	open(fname,"a").write("\n"+str(entry)+"\n")

def send_headers(clientsocket):
	server_header = [
									"HTTP/1.0 200 OK\r\n",
									"Content-Type: text/html\r\n",
									"Server: Rickys Webserver\r\n",
									"Cache-Control: max-age=3600\r\n",
									"Alow: GET\r\n",
									"Connection: keep-alive\r\n",
									"\r\n"]
	if clientsocket:
		for peram in server_header:
			clientsocket.sendall(peram)

def parseRequestHeaders(raw_request):
	return raw_request.splitlines()
	
def send_file(clientsocket,fname):
	try:
		if clientsocket:
			for line in open(fname,"r").readlines():
				clientsocket.sendall(line+"<hr/>")
	except:
		pass

def spider_links(clientsocket,limit):
	try:
		if clientsocket:
			for link in LINKS(limit):
				link = "<a href='%s'>%s</a><hr/><br/>" % (link['link'],link['link'])
				clientsocket.sendall(link)
	except:
		pass

def spider_sites(clientsocket):
	for site in sites():
		clientsocket.sendall(site)
	

def server(host,port):
	#create an INET, STREAMing socket
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#bind the socket to a public host,
	# and a well-known port
	serversocket.bind((host,port))
	#become a server socket
	serversocket.listen(5)
	
	while 1:
		try:
			#accept connections from outside
			(clientsocket, address) = serversocket.accept()
			# request is the raw http request header sent
			# from the client
			request = clientsocket.recv(1000000)
			# request_header is the parsed request header
			# it's data type is a list
			request_header = parseRequestHeaders(request)
			print request_header
			# Log the request sent by the client 
			log("access.log","Client:" + address[0] + "\n" + request)
			send_headers(clientsocket)
			# Send the content
			#send_file(clientsocket,"../meta-spider/sites.txt")
			#spider_links(clientsocket,1000)
			spider_sites(clientsocket)
			# Close the connection to the client
			clientsocket.close()
		except socket.error:
			pass
server = server("127.0.0.1",8000)
	
