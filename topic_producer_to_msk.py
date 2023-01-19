# ==========================================
# PRODUCER
# ==========================================
from confluent_kafka import Producer
from time import sleep
from random import random
import json
import datetime

conf = {}
conf[
    "bootstrap.servers"
] = "b-1-#####.ap-northeast-2.amazonaws.com:9196, b-2-#####.ap-northeast-2.amazonaws.com:9196"
conf["security.protocol"] = "SASL_SSL"
conf["sasl.mechanism"] = "SCRAM-SHA-512"
conf["sasl.username"] = "#####"
conf["sasl.password"] = "#####"
print(conf)

producer = Producer(conf)
topic = "test_stream_data_2"
counter = 1


while True:
    data = {
        "plant_name": "지영발전소",
        "plant_id": 99,
        "type": "per_second",
        "generation": 99 + random(),
        "time": (datetime.datetime.now() - datetime.timedelta(hours=2)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
    }
    producer.produce(topic, value=json.dumps(data))
    print("Sample #{} produced!".format(counter))
    counter += 1
    producer.flush(1)
    sleep(1)
