# ==========================================
# PRODUCER
# ==========================================
from confluent_kafka import Producer
from time import sleep
from random import random
import json

conf = {"bootstrap.servers": "localhost:9092"}
producer = Producer(conf)
topic = "faust_stream_data_11"
counter = 1

while True:
    data = {
        "plant_name": "지영발전소",
        "plant_id": 99,
        "type": "per_second",
        "generation": 99 + random(),
    }
    producer.produce(topic, value=json.dumps(data))
    print("Sample #{} produced!".format(counter))
    counter += 1
    producer.flush(1)
    sleep(1)
