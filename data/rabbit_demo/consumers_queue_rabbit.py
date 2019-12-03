# -*- coding: utf-8 -*-
# Author: Hardy
# Date: 2019-11-05
# Description: rabbit 消费者
import pika
import time

from rabbit_conf import RABBIT_HOST, RABBIT_PORT, RABBIT_USER, RABBIT_PASS

credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)
conn = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST,
                                                         RABBIT_PORT,
                                                         '/',
                                                         credentials))
channel = conn.channel()
channel.queue_declare(queue='hardy', durable=True)  # 持久化队列


def callback(ch, method, properties, body):
    print(f"{time.strftime('%H:%M:%S')}:收到消息 {body}")


channel.basic_consume('hello',
                      callback,
                      no_ack=False,  # 消费完毕向服务端发送一个确认
                      consumer_tag="hello-consumer")

print(f"{time.strftime('%H:%M:%S')}:等待消息，按CTRL+C退出")
channel.start_consuming()



