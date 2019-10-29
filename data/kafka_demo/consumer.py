from kafka import KafkaConsumer
from kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

consumer = KafkaConsumer(KAFKA_TOPIC,
                         bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS])
for message in consumer:
    print(message)
