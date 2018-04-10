from assets import Global
from connectKafka import prod

def sendData(numbers,similarity,topic):
    prod.run(numbers,similarity,topic)