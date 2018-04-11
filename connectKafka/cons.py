from kafka import KafkaConsumer
import msgpack

def run(titles=[],articles = [],topic=""):
    consumer = KafkaConsumer(topic,bootstrap_servers='203.77.73.194:32772',consumer_timeout_ms=10000,auto_offset_reset='earliest',enable_auto_commit=False)
    for msg in consumer:
        # print(msgpack.unpackb(msg.value,raw=False))
        data = msgpack.unpackb(msg.value,raw=False)
        titles.append(data["title"])
        articles.append(data["article"])

            # print(type())
def Print(topic):
    consumer = KafkaConsumer(topic,bootstrap_servers='203.77.73.194:32772',consumer_timeout_ms=10000,auto_offset_reset='earliest',enable_auto_commit=False)
    for msg in consumer:
        try:
            print(msgpack.unpackb(msg.value,raw=False))
        except:
            print("[略]")