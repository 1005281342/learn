import pika

# 建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"
                                                               ))
# 创建channel
channel = connection.channel()
# 创建名字为hello的queue
channel.queue_declare(queue="hello")
# 默认交易所，我们通过空字符串 (“”)来标识
channel.basic_publish(exchange="", routing_key="hello", body="Hello MQ5")
connection.close()
