import requests
import time
import json
from assets import Global
from bs4 import BeautifulSoup

def get_articles():
	res = requests.get(Global.YAHOO_URL,headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text,"html.parser")

	articles = [] 
	#all_li = soup.select('div[id="YDC-Stream"] > ul > li') 
	for li in soup.find_all('li',{'class':'js-stream-content Pos(r)'}):
		if(len(li.div.div.find_all('span')) >= 2):
			print(li.div.div.find_all('span')[0].text)
			print(li.div.div.find_all('span')[1].text)
			print(li.div.div.h3.find('a').text)   #標題
			print(li.div.div.h3.find('a')['href'])
			print('')
			link = 'https://tw.news.yahoo.com'+str(li.div.div.h3.find('a')['href'])
			co_res = requests.get(link,headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
			co_res.encoding = 'utf8'
			co_soup = BeautifulSoup(co_res.text,"html.parser")
			if(co_soup.find('article',{'itemprop':'articleBody'})):
				for p in co_soup.find('article',{'itemprop':'articleBody'}).find_all('p'): #content
					try:
						print(p.text)
					except:
						print("\n.\n")



