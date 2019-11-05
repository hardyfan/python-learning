[参考链接](https://python-socketio.readthedocs.io/en/latest/)

# 服务端


# 客户端

## 命名空间
```
sio.connect('http://localhost:5000', namespaces=['/chat'])

@sio.event(namespace='/chat')
def my_custom_event(sid, data):
    pass

@sio.on('connect', namespace='/chat')
def on_connect():
    print("I'm connected to the /chat namespace!")

sio.emit('my message', {'foo': 'bar'}, namespace='/chat')
```
