import urllib.request
import requests
import bs4
page = urllib.request.urlopen('http://doraithodla.com/')
responsesoup = bs4.BeautifulSoup(page.read())
links=[]
for link in responsesoup.find_all('li > a'):
	print (link.get('href'))

# print (links) 
# content = ''
# title = ''
# for link in responsesoup.find_all('div' , {'class': 'entry-content'}):
# 	content =link.text
# for link in responsesoup.find_all('h1' , {'class': 'entry-title'}):
# 	title = link.text

# r = requests.post("http://localhost:8000/wiki/api/add/"+title+"/", data={'content':content})
# print(r.status_code, r.reason)
