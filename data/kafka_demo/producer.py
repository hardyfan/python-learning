import time
import json
from kafka import KafkaProducer
from kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
i = 0
while i < 5:
    ts = int(time.time() * 1000)
    data = {
        "value": f'value{i}',
        "key": f'key{i}',
        "time": ts
    }
    data = json.dumps(data)
    producer.send(KAFKA_TOPIC, data.encode("utf-8"))
    producer.flush()
    i += 1
    print(f"send {i}")
    time.sleep(1)

