import urllib.request
import bs4
from bs4 import BeautifulSoup
import requests
links=[]
url = "http://doraithodla.com/"

page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page)
li = soup.select("ul > li > a")
for link in li:
    links.append(link.get('href'))
# for each in links:

# url1 = each
url1=links[4]
print(url1)
links1=[]
page1 = urllib.request.urlopen(url1).read()
soup1 = BeautifulSoup(page1)
li1 = soup1.findAll('a', rel="bookmark")
for x in li1:
	links1.append(x.get('href'))
links2=list(set(links1))
print(links2)
for y in links2:
	page2 = urllib.request.urlopen(y)
	responsesoup = bs4.BeautifulSoup(page2.read())
	content = ''
	title = ''
	for link2 in responsesoup.find_all('div' , {'class': 'entry-content'}):
		content =link2.text
	for link2 in responsesoup.find_all('h1' , {'class': 'entry-title'}):
		title = link2.text

	r = requests.post("http://localhost:8000/wiki/api/add/"+title+"/", data={'content':content})
	print(r.status_code, r.reason)