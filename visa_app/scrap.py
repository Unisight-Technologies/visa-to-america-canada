import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request('https://www.cicnews.com/latest-immigration-news.html', headers={'User-Agent': 'Mozilla/5.0'})
URL = "https://www.cicnews.com/latest-immigration-news.html#gs.n3b9io"
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

title=[] # a list to store quotes


for div in soup.findAll('span',
						attrs = {'class':'entry-title-primary'}):

	title.append(div.text.strip())
print(title)
