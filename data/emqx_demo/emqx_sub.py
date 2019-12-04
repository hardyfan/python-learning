# -*- coding: utf-8 -*-
# FileName: emqx_sub.py
# Create by Hardy on 2019-12-04
# Description:
import paho.mqtt.client as mqtt
from datetime import datetime

from emqx_conf import EMQX_HOST, EMQX_PORT


def on_connect(client, user_data, flags, rc):
    print(f'connected {str(rc)}')


def on_message(client, user_data, msg):
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}:{msg.topic} {str(msg.payload)}')


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(EMQX_HOST, EMQX_PORT, 600)
    client.subscribe('hardy', qos=0)
    client.loop_forever()

