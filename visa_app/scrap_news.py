import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pprint

def get_title(soup):
	titles = []
	count=0
	for div in soup.findAll('span',
							attrs = {'class':'entry-title-primary'}):
		count+=1
		if(count<6):
			titles.append(div.text.strip())
		else:
			break
	return titles

def get_combined(soup):
	description = []
	count1=0
	for div in soup.findAll('div',
							attrs = {'class':'text'}):
		count1+=1
		if(count1<6):
			description.append(div.text.strip())
		else:
			break

	return description


def get_author(description, soup):
	authors = []
	for author in description:
		temp=author.split('\n\n')
		authors.append(temp[1])
	return authors


def get_description(description, soup):
	final_description = []
	for author in description:
		temp=author.split('\n\n')
		final_description.append(temp[0])
	return final_description

def get_url(soup):
	urls = []
	found=False
	counter=0
	for a in soup.findAll('a', href=True):
		if(found and counter<15):
			if(counter%3==0):
				urls.append(a['href'])
			counter+=1

		if(a['href']=='https://www.cicnews.com'):
			found=True
	return urls

def get_url_images(soup):
	url_images = []
	counter1=0
	images=soup.findAll('img')
	for image in images:
		counter1+=1
		if(counter1>5 and counter1<11):
			url_images.append(image['src'])

	return url_images




class Scrapper():
	def __init__(self):
		req = Request('https://www.cicnews.com/latest-immigration-news.html', headers={'User-Agent': 'Mozilla/5.0'})
		URL = "https://www.cicnews.com/latest-immigration-news.html#gs.n3b9io"
		html = urllib.request.urlopen(req).read()
		soup = BeautifulSoup(html, 'html.parser')

		self.titles = get_title(soup)
		self.combined = get_combined(soup)
		self.authors = get_author(self.combined, soup)
		self.descriptions = get_description(self.combined, soup)
		self.urls = get_url(soup)
		self.url_images = get_url_images(soup)


# urllib.request.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")

# TODO: SCRAP CANADA.CA WEBSITE---------------------------------->
# def canada_ca(title):
# req = Request('https://www.canada.ca/en/news.html')
# URL = "https://www.canada.ca/en/news.html"
# html = urllib.request.urlopen(req).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# title=[]
# #
# # for div in soup.findAll('td',
# # 						attrs = {'class':'nws-tbl-ttl h4'}):
# # 	# print(div.text.strip())
# #
# # 	title.append(div.contents)
# # print(title)
#
# for tr in soup.find_all('tr')[2:]:
#     tds = tr.find_all('td')
#     print  (tds[0].text)
