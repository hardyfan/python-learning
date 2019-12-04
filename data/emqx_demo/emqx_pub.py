# -*- coding: utf-8 -*-
# FileName: emqx_pub.py
# Create by Hardy on 2019-12-04
# Description:
import paho.mqtt.client as mqtt
import time
from datetime import datetime

from emqx_conf import EMQX_HOST, EMQX_PORT


def on_connect(client, user_data, flags, rc):
    print(f'connected {str(rc)}')


def on_publish(client, msg, mid):
    print(f'{datetime.now().strftime("%H:%M:%S Send ")}:{msg.topic} {str(msg.payload)}')


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(EMQX_HOST, EMQX_PORT, 600)
    while True:
        client.publish('hardy', payload='hello mqtt', qos=0)
        print(f'{datetime.now().strftime("%H:%M:%S")}: hardy SEND hello mqtt')
        time.sleep(3)
    client.loop_forever()



