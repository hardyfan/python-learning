# -*- coding: utf-8 -*-
# Author: Hardy
# Date: 2019-11-05
# Description: rabbit 生产者

import pika
import time

from rabbit_conf import RABBIT_HOST, RABBIT_PORT, RABBIT_USER, RABBIT_PASS

credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)
conn = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST,
                                                         RABBIT_PORT,
                                                         '/',
                                                         credentials))
channel = conn.channel()
channel.queue_declare(queue='hello')

for i in range(5):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=f'{i+1}:Hello World!')

print(f"{time.ctime()}:开始队列...")
conn.close()


