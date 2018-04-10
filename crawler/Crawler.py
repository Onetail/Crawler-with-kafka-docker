import requests
import time
import json
import jieba
from bs4 import BeautifulSoup
from assets import Global
from crawler import CosineSimilarity as cs

def get_articles(url,topic):
	res = requests.get(url,headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text,"html.parser")

	articles = []
	titles = []
	#all_li = soup.select('div[id="YDC-Stream"] > ul > li') 
	for li in soup.find_all('li',{'class':'js-stream-content Pos(r)'}):
		if(len(li.div.div.find_all('span')) >= 2):
			try:
				print(li.div.div.find_all('span')[0].text)
				print(li.div.div.find_all('span')[1].text)
				print(li.div.div.h3.find('a').text)   #標題
				print(li.div.div.h3.find('a')['href'])
				print('')
				titles.append(li.div.div.h3.find('a').text)
			except:
				pass 
			link = 'https://tw.news.yahoo.com'+str(li.div.div.h3.find('a')['href'])
			co_res = requests.get(link,headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
			co_res.encoding = 'utf8'
			co_soup = BeautifulSoup(co_res.text,"html.parser")
			if(co_soup.find('article',{'itemprop':'articleBody'})):
				news_string = ""
				for p in co_soup.find('article',{'itemprop':'articleBody'}).find_all('p'): #content
					news_string += p.text
				articles.append(" ".join(jieba.cut(news_string,cut_all=False)))
				
	articles_sim,articles_number = cs.jiebaAnalyse(articles)
	cs.comparisonSimilarity(articles_sim,articles_number,titles,topic)

