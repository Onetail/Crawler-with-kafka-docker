import jieba
import jieba.analyse
import numpy
import csv
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from assets import Global
from crawler import SendtoKafka as StoK

def jiebaAnalyse(corpus=[""]):
	jieba.set_dictionary('./example/dict.txt.big')
	vectorizer = TfidfVectorizer()
	tfidf = vectorizer.fit_transform(corpus)
	fv = tfidf.toarray()
	print(tfidf.shape)
	words = vectorizer.get_feature_names()
	for i in range(len(corpus)):
		pass

	return tfidf,i+1
		
def comparisonSimilarity(articles,number,titles,topic):
	
	# clear .csv file data
	similarity = []
	numbers = []
	# print(titles)
	for i in range(number):
		for j in range(number):
				if not i == j :
					# print(j)
					# print(titles[j])
					similarity.append(cosine_similarity(articles[i],articles[j])[0])
					try:
						app = titles[i]+","+titles[j]
					except:
						pass
					numbers.append(app)
		#排序
		bubbleSort(number,similarity,numbers)

		for z in range(number):
		# for j in range(len(similarity[i])):
			if z < 5 and not i == z:
				print("{:} ".format(numbers[z].split(",")[0]))
				print(" {:} ".format(numbers[z].split(",")[1]))
				print(similarity[z])
		# build csv file
		csvWrite(numbers,similarity)
		# to kafka consumer
		# StoK.sendData(numbers,similarity,topic)
		similarity = []
		numbers = []


def bubbleSort(number,similarity,numbers):
	for i in range(len(similarity)):
		for j in range(len(similarity)):
			
			if similarity[i]>similarity[j]:
				temp = similarity[i]
				similarity[i] = similarity[j]
				similarity[j] = temp 
				tmp = numbers[i]
				numbers[i] = numbers[j]
				numbers[j] = tmp

def csvWrite(numbers,similarity):
	with open(Global.CRAWLER_FILE_NAME,"a") as csv_file:
		csv_writer = csv.writer(csv_file)
		getdata=[numbers[0].split(",")[0]]
		getdata+=[numbers[i].split(",")[1] for i in range(Global.TOP_NEWS_NUMBER)]
		csv_writer.writerow(getdata)
		
	
def makeCsv():
	with open(Global.CRAWLER_FILE_NAME,"w") as csv_file:
		pass
		

