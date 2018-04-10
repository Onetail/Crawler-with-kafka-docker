from kafka import KafkaConsumer

def run(topic=""):
    consumer = KafkaConsumer(bootstrap_servers='203.77.73.194:32797',consumer_timeout_ms=1000)
    consumer.subscribe([topic])
    while(1):
        for msg in consumer:
            print(str(msg.value,encoding='utf-8'))
            # print(type())