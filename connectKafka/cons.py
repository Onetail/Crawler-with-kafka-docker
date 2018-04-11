from kafka import KafkaConsumer

def run(topic=""):
    consumer = KafkaConsumer('aaasssddd',bootstrap_servers='203.77.73.194:32797',consumer_timeout_ms=1000)
    
    while(1):
        for msg in consumer:
            print(str(msg.value))
            # print(type())