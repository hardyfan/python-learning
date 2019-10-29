import time
import json
from kafka import KafkaProducer
from kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
i = 0
while i < 10:
    ts = int(time.time() * 1000)
    data = {
        "value": str(i),
        "key": str(i),
        "time": ts
    }
    data = json.dumps(data)
    producer.send(KAFKA_TOPIC, data.encode("utf-8"))
    producer.flush()
    print(i)
    i += 1
    time.sleep(1)

