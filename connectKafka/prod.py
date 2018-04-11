from kafka import KafkaProducer
from assets import Global
import msgpack

def run(title,content,topic):
    producer = KafkaProducer(bootstrap_servers='203.77.73.194:32772',value_serializer=msgpack.dumps)
    getdata= ""
    
    dic = {'title':title,'article':content}
    producer.send(topic,dic)
    producer.flush()
