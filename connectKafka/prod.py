from kafka import KafkaProducer

def run(numbers,similarity,topic):
    producer = KafkaProducer(bootstrap_servers='203.77.73.194:32797')
    getdata=[numbers[0].split(",")[0]]
    getdata+=[numbers[i].split(",")[1] for i in range(Global.TOP_NEWS_NUMBER)]
    producer.send(topic,b'{:}'.format(getdata))
