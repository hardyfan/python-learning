# -*- coding: utf-8 -*-
# FileName: producer_exchange_rabbit.py
# Create by Hardy on 2019-12-03
# Description:
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

for i in range(6):
    message = f'{i+1}:Hello Hardy!'
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=message)

print(f"{time.ctime()}:开始队列...")
conn.close()



