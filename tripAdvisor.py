import urllib2
from bs4 import BeautifulSoup
from pymongo import MongoClient # the mongo client


req = urllib2.urlopen('http://www.tripadvisor.in/Attraction_Review-g297596-d1204434-Reviews-Sukhna_Lake-Chandigarh.html')
html = req.read()
soup = BeautifulSoup(html)
name = soup.find('h1', {'class': 'header'})
#print name.text
name = name.text

location = soup.find('span', {'property':'v:municipality'})
#print location.text
location = location.text

likes = soup.find('span', {'class': 'percent'})
#print likes.text
likes = likes.text


rank = soup.find('b', {'class': 'rank_text'})
rank = rank.text
#print rank.text

tags = soup.find('div', {'class': 'detail'})
# print tags.text.strip().split(':')[1].strip().split(',')
tags = tags.text.strip().split(':')[1].strip().split(',')

#connecting to database
client = MongoClient('mongodb://localhost:27017/')
try:
	db = client['testingPy'] 	#connect to db
	col = db['class']
except Exception, e: print e

data = {
	"locationName": name,
	"city": location,
	"likes": likes,
	"rank": rank,
	"tags": tags
	}
# inserting data into mongo collection named 'class' and db = 'testingPy'
col.insert(data)