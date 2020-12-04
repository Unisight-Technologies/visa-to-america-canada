import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pprint

class Scrapper():
	def __init__(self):
		self.title=


def cic_news():

	req = Request('https://www.cicnews.com/latest-immigration-news.html', headers={'User-Agent': 'Mozilla/5.0'})
	URL = "https://www.cicnews.com/latest-immigration-news.html#gs.n3b9io"
	html = urllib.request.urlopen(req).read()
	soup = BeautifulSoup(html, 'html.parser')

	title=[] # a list to store titles
	description=[]
	url_images=[]
	authors=[]
	final_description=[]
	urls=[]


	count=0
	for div in soup.findAll('span',
							attrs = {'class':'entry-title-primary'}):
		count+=1
		if(count<6):
			title.append(div.text.strip())
		else:
			break



	count1=0
	for div in soup.findAll('div',
							attrs = {'class':'text'}):
		count1+=1
		if(count1<6):
			description.append(div.text.strip())
		else:
			break

	for author in description:
		temp=author.split('\n\n')
		final_description.append(temp[0])
		authors.append(temp[1])

	found=False
	counter=0
	for a in soup.findAll('a', href=True):
		if(found and counter<15):
			if(counter%3==0):
				urls.append(a['href'])
			counter+=1

		if(a['href']=='https://www.cicnews.com'):
			found=True



	counter1=0
	images=soup.findAll('img')
	for image in images:
		counter1+=1
		if(counter1>5 and counter1<11):
			url_images.append(image['src'])



	pprint.pprint(authors)
	print('\n\n')
	pprint.pprint(urls)
	print('\n\n')
	pprint.pprint(title)
	print('\n\n')
	print(final_description)
	print('\n\n')
	pprint.pprint(url_images)
	print('\n\n')

for i in range(0,5):
	news = models.News.objects.create(
		author=authors[i],
		title=title[i],
		description=final_description[i],
		url=urls[i]
	)
	news.save()

cic_news()
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
