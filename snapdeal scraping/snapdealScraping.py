import urlparse
import urllib
import bs4
from bs4 import BeautifulSoup

url = "https://www.snapdeal.com/product/mi4i-16gb/654856488809#bcrumbSearch:redmi"
fo = open("new.txt", "w+")


#_3eAQiD

htmltext = urllib.urlopen(url).read()
soup = BeautifulSoup(htmltext, "html.parser")
table = soup.findAll('table')

for i in range(len(table)):
	rows = table[i].findAll('tr')
	h = table[i].findAll('th')
	i=0;
	for tr in rows:
		i=i+1;
		if(i%2==1):
			cols = tr.findAll('td')
			for td in cols:
				text = td.find(text=True).strip()
				if(text!=""):
					fo.write(text)
					fo.write(':')	
			fo.write('\n')
	fo.write('\n')
print "End"