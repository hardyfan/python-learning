# -*- coding: utf-8 -*-
# Author: Hardy
# Date: 2019-11-05
# Description: socket 服务端

import socketio
from aiohttp import web
from socket_conf import SOCKET_HOST, SOCKET_PORT

app = web.Application()
sio = socketio.AsyncServer()
sio.attach(app)


@sio.on('topic_receive')
async def receive_message(sid, msg):
    print(f'Socket ID: {sid}, Message:{msg}')
    await sio.emit('topic_send', msg)


async def index(request):
    return web.Response(text="socket.IO server is running",
                        content_type='text/html')


if __name__ == '__main__':
    app.router.add_get('/', index)
    web.run_app(app, host=SOCKET_HOST, port=SOCKET_PORT)

