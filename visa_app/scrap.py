import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import pprint

URL = "http://www.values.com/inspirational-quotes"
html = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html, 'html.parser')

title=[] # a list to store quotes


for div in soup.findAll('span',
						attrs = {'class':'entry-title-primary'}):

	title.append(title)
print(title)
