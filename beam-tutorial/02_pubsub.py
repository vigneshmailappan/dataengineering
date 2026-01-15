
from google.cloud import pubsub_v1

# Config
project_id = "local-project"
topic_id = "test-topic"
sub_id = "test-sub"

# Clients
publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

# Paths
topic_path = publisher.topic_path(project_id, topic_id)
sub_path = subscriber.subscription_path(project_id, sub_id)

# Create topic
try:
    publisher.create_topic(request={"name": topic_path})
    print("✅ Topic created:", topic_path)
except Exception:
    print("ℹ️ Topic already exists:", topic_path)

# Create subscription
try:
    subscriber.create_subscription(request={"name": sub_path, "topic": topic_path})
    print("✅ Subscription created:", sub_path)
except Exception:
    print("ℹ️ Subscription already exists:", sub_path)

# Publish one test message
print("Publishing test message...")
future = publisher.publish(topic_path, b'{"score": 123}')
print("✅ Published message ID:", future.result())

# Pubsub
# Publisher - Subscriber - Message

# publisher - sender of message 
# topic - mailbox 
# subscriber - receiver of message
#   types : pull | push
#       pull :
#           Messages will stay in topic ( mailbox ) until user picks up
#       push : 
#           messages will be delivered automatically upon arrival.
#       NOTE : BEAM SUPPORTS ONLY PULL SUBSCRIPTION. WORKERS OF BEAM RUNNER CONTINUOUSLY PULLS MESSAGES
# 
# 
# emulator : 
#   we are using pubsub emulator to run things locally. with emulator we can only use python to handle pubsub. 
# 
# 
# 