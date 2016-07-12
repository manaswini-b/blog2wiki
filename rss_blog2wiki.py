import urllib.request
import bs4
from bs4 import BeautifulSoup
import requests
from xml.etree import ElementTree as etree
ns = {'dc': 'http://purl.org/dc/elements/1.1/','content': 'http://purl.org/rss/1.0/modules/content/'}
def letters(input):
    valids = []
    for character in input:
        if character.isalpha() or character == ' ':
            valids.append(character)
    return ''.join(valids)
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
	# links1=[]
	# page1 = urllib.request.urlopen(url1).read()
	# soup1 = BeautifulSoup(page1)
	# li1 = soup1.findAll('h2', {'class': 'entry-title'})
	# for i in li1:
	# 	li2 = i.findAll('a', rel="bookmark")
	# 	for x in li2:
	# 		links1.append(x.get('href'))
	# links2=list(set(links1))
	# for y in links2:
	# 	page2 = urllib.request.urlopen(y)
	# 	responsesoup = bs4.BeautifulSoup(page2.read())
	# 	content = ''
	# 	title = ''
	# 	content = responsesoup.find('div' , {'class': 'entry-content'})
	# 	title = responsesoup.find('h1' , {'class': 'entry-title'})
	# 	r = requests.post("http://wiki.infoassistants.net/wiki/api/add/"+title.text.replace("?", "") +"/", data={'content': content.encode('utf-8') , 'cate': cate1 })
	# 	print(r.status_code, r.reason)
	# 	if(r.status_code, r.reason == "404 Not Found"):
	# 		error_catch.append(y)
	# print (links[each]+'rss')
	reddit_file = urllib.request.urlopen(links[each]+'rss')
	reddit_data = reddit_file.read()
	reddit_file.close()

	reddit_root = etree.fromstring(reddit_data)
	item = reddit_root.findall('channel/item')
	reddit_feed={}
	for entry in item:   
	    reddit_feed[entry.findtext('title')] = entry.find('content:encoded',ns).text

	for i in reddit_feed:
		r = requests.post("http://localhost:8000/wiki/api/add/"+i.replace("?","__").replace("/","^^")+"/", data={'content':reddit_feed[i],'cate':cate[each]})
		# print(r.status_code)
		if r.status_code == 404:
			print (cate[each]+' : '+str(i.encode('utf-8')))