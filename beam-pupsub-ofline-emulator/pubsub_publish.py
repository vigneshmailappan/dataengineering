import pubsub_emulate as pse

print("Publishing test message...")

future = pse.publisher.publish(
    pse.topic_path,
    b'{"score": 123}',
)
print("Published message ID:", future.result())