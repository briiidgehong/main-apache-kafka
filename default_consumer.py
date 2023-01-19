# ==========================================
# CONSUMER
# ==========================================
from kafka import KafkaConsumer
from json import loads

topic = "hz_generation"

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="my-group52",
    value_deserializer=lambda x: loads(x.decode("utf-8")),
    consumer_timeout_ms=1000,
)

# consumer list를 가져온다
print("[begin] get consumer list")
print(consumer)

while True:
    for message in consumer:
        msg = f"{message.topic}, {message.partition}, {message.offset}, {message.key}, {message.value}"
        print(
            "Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s"
            % (
                message.topic,
                message.partition,
                message.offset,
                message.key,
                message.value,
            )
        )

print("[end] get consumer list")
