import requests
import time
import json
import jieba
from bs4 import BeautifulSoup
from assets import Global
from crawler import CosineSimilarity as cs
from crawler import SendtoKafka as StoK
from kafka import KafkaConsumer
import msgpack


def get_articles(url,topic):

	consumer = KafkaConsumer('entertainment',bootstrap_servers='203.77.73.194:32772',consumer_timeout_ms=5000,auto_offset_reset='earliest',enable_auto_commit=False)
	titleList = []
	for msg in consumer:
		titleList.append(msgpack.unpackb(msg.value,raw=False)['title'])


	res = requests.get(url,headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text,"html.parser")
	title = ""
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
				title = li.div.div.h3.find('a').text
				# titles.append(li.div.div.h3.find('a').text)
				
			except:
				pass 
			link = 'https://tw.news.yahoo.com'+str(li.div.div.h3.find('a')['href'])
			co_res = requests.get(link,headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
			co_res.encoding = 'utf8'
			co_soup = BeautifulSoup(co_res.text,"html.parser")
			if(co_soup.find('article',{'itemprop':'articleBody'})):
				if title not in titleList:
					news_string = ""
					for p in co_soup.find('article',{'itemprop':'articleBody'}).find_all('p'): #content
						news_string += p.text
				# articles.append(" ".join(jieba.cut(news_string,cut_all=False)))
				
					StoK.sendData(title,news_string,topic)		
		
	StoK.getData(titles,articles,topic)
	articles_sim,articles_number = cs.jiebaAnalyse(articles)
	cs.comparisonSimilarity(articles_sim,articles_number,titles,topic)

