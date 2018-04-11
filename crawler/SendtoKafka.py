from assets import Global
from connectKafka import prod,cons

def sendData(title,content,topic):
    prod.run(title,content,topic)

def getData(titles,articles,topic):
    cons.run(titles,articles,topic)    