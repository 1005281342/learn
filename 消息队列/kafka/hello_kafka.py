# 连接
from kafka import KafkaConsumer
from kafka import KafkaProducer

server_list = ["192.168.0.1:xxxx", "192.168.0.2:xxxx"]
# 生产者
producer = KafkaProducer(bootstrap_servers=server_list, compression_type='gzip')
msg = {"name": "小飞1", "text": "测试1"}
bmsg = bytes(str(msg).encode('utf-8'))
producer.send('xiaofei_test', bmsg)
# 消费者
consumer = KafkaConsumer('xiaofei_test', auto_offset_reset='earliest', bootstrap_servers=server_list)
print(consumer)
for msg in consumer:
    print(msg)

# 生产者
from pykafka import KafkaClient
import json

hosts = "192.168.0.1:xxxx,192.168.0.2:xxxx"
client = KafkaClient(hosts=hosts)
print(client.topics)
key = "test"
key = bytes(key, encoding='utf8')
topic = client.topics[key]

# 因为是简单使用, 所以没有分组, 只是用topic 当redis中的key使用
producer = topic.get_producer(sync=True)
producer.start()
print(producer)
# 生产消息
msg_dict = {"test": "测试数据"}

msg = json.dumps(msg_dict)
with topic.get_sync_producer() as producer:
    producer.produce(bytes(msg, encoding='utf8'))
    print(msg)
    print('插入成功')

# 消费者
from pykafka import KafkaClient

hosts = "192.168.0.1:xxxx,192.168.0.2:xxxx"
client = KafkaClient(hosts=hosts)

print("Kafka client:", client.topics)

# 消费者
key = "chengdu-cdfgjtj-research_details"
key = bytes(key, encoding='utf8')
topic = client.topics[key]
# 一些参数信息可以看一下 https://www.cnblogs.com/jun1019/p/6656223.html
consumer = topic.get_simple_consumer(auto_commit_enable=True)
# consumer = topic.get_simple_consumer(consumer_group='test', auto_commit_enable=True, consumer_id='test')
for message in consumer:
    if message is not None:
        print("consumer message:", message.offset)
        print(message.value)
