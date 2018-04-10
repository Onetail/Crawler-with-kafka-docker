from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='203.77.73.194:32797')
while(1):
    producer.send('aaasssddd',b'msg')
