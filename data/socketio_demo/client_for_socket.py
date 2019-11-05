# -*- coding: utf-8 -*-
# Author: Hardy
# Date: 2019-11-05
# Description:socket 客户端

import socketio
import time
import json
from socket_conf import SOCKET_URL

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def disconnect():
    print('disconnected from server')


@sio.event
def topic_send(data):
    print('take topic:', data)


sio.connect(SOCKET_URL)

# 模拟定时发送一些数据
n = 0
while n < 5:
    n += 1
    time.sleep(3)
    msg = {
        'Name': 'Hardy',
        'Gender': 'Man',
        'Old': '42',
        'Degree': 'Bachelor'
    }
    sio.emit('topic_receive', msg)
    print("send topic: ", msg)

sio.wait()



