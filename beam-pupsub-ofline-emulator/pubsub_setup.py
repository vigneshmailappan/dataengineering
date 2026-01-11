import pubsub_emulate as pse

# Create topic
try:
    pse.publisher.create_topic(request={"name": pse.topic_path})
    print("Topic created")
except Exception as e:
    print("Topic already exists")

# Create subscription
try:
    pse.subscriber.create_subscription(
        request={"name": pse.sub_path, "topic": pse.topic_path}
    )
    print("Subscription created")
except Exception as e:
    print("Subscription already exists")

