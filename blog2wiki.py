import urllib.request
import bs4
from bs4 import BeautifulSoup
import requests
links=[]
cate = []
url = "http://doraithodla.com/"
error_catch = []
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page)
li = soup.select("ul > li > a")
for link in li:
    links.append(link.get('href'))
    cate.append(link.text)
for each in range(len(links)):
	url1=links[each]
	cate1 = cate[each]
	links1=[]
	page1 = urllib.request.urlopen(url1).read()
	soup1 = BeautifulSoup(page1)
	li1 = soup1.findAll('h2', {'class': 'entry-title'})
	for i in li1:
		li2 = i.findAll('a', rel="bookmark")
		for x in li2:
			links1.append(x.get('href'))
	links2=list(set(links1))
	for y in links2:
		page2 = urllib.request.urlopen(y)
		responsesoup = bs4.BeautifulSoup(page2.read())
		content = ''
		title = ''
		content = responsesoup.find('div' , {'class': 'entry-content'})
		title = responsesoup.find('h1' , {'class': 'entry-title'})
		r = requests.post("http://wiki.infoassistants.net/wiki/api/add/"+title.text.replace("?", "") +"/", data={'content': content.encode('utf-8') , 'cate': cate1 })
		print(r.status_code, r.reason)
		if(r.status_code, r.reason == "404 Not Found"):
			error_catch.append(y)

print (error_catch)