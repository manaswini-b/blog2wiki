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
	reddit_file = urllib.request.urlopen(links[each]+'rss')
	reddit_data = reddit_file.read()
	reddit_file.close()

	reddit_root = etree.fromstring(reddit_data)
	item = reddit_root.findall('channel/item')
	reddit_feed={}
	for entry in item:   
	    reddit_feed[entry.findtext('title')] = [entry.find('content:encoded',ns).text,entry.findtext('pubDate')]

	for i in reddit_feed:
		tmp = reddit_feed[i][1].split(" ")
		month_dict={"Jan":"January", "Feb":"February", "Mar":"March", "Apr":"April", "May":"May","Jun":"June","Jul": "July","Aug":"August", "Sep":"September", 
	"Oct":"October", "Nov":"November", "Dec":"December"}
		date = tmp[1]+" "+month_dict[tmp[2]]+" "+tmp[3]
		r = requests.post("http://wiki.infoassistants.net/wiki/api/add/"+i.replace("?","__").replace("/","^^")+"/", data={'content':reddit_feed[i][0],'cate':cate[each],'date':date})
		# print(r.status_code)
		if r.status_code == 404:
			print (cate[each]+' : '+str(i.encode('utf-8')))