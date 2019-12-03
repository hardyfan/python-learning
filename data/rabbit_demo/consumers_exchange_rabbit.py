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
channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)


def callback(ch, method, properties, body):
    print(f"{time.strftime('%H:%M:%S')}:收到消息 {body}")


channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)

print(f"{time.strftime('%H:%M:%S')}:等待消息，按CTRL+C退出")
channel.start_consuming()



