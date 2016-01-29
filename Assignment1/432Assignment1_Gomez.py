#CS432_Assignment1_Gomez
#Matthew Gomez
#UIN: 009335568
#1/28/16
#Web Info - curl
#Dr.Nelson

import httplib2
import urllib2
import sys
import requests
from bs4 import BeautifulSoup

#Command Line Arguments 
print (sys.argv)

#URL Place Holder for argv
URLName= sys.argv[1]


#URL Reader
website = urllib2.urlopen( URLName )
websiteFile = website.read()
website.close()

#Link Extraction-Extract the Links from the URI
soup=BeautifulSoup(websiteFile)
#Function
def LinkExtractor(Linklist):
	for item in Linklist:
		if item ["redirections"]==None:
			print ("{0} {1}".format(item["uri"],item["size"]))
		else:
			print ("{0}".format(item["uri"]))
			for drctLink in item["redirections"]:
				print ("\t{0}".format(drctLink))
			print ("\t{0}".format(item["size"]))

#Link Handeler 
def linkHandler (link):
#Creating a request.
	request = urllib2.Request(link)

#Getting a response
	response = urllib2.urlopen(request)
#Checking the Content Type
	
	value1=response.info().getheader('Content-Type')
	value1=value1.split("/")[1]

	num_bytes=None
	redirectedLinks=None
	linkPDF=False


	if value1 =='pdf':1
	linkPDF=True
	num_bytes = response.info().getheader('content-length')




	

#Redirection
	if response.geturl()!= link:
		redirectedLinks=[]
		redirectedLinks.append(response.geturl())
	result = {}
	result["uri"]=link
	result["linkPDF"]=linkPDF
	result["redirections"]=redirectedLinks
	result['size']=num_bytes
	return result

linkerpdf=[]

for links in soup.find_all('a'):
	res=linkHandler(links.get('href'))
	if res["linkPDF"]==True:
		linkerpdf.append(res)
LinkExtractor(linkerpdf)


