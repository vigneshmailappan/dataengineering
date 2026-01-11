from google.cloud import pubsub_v1
import os

os.environ["PUBSUB_EMULATOR_HOST"] = "localhost:8085"
os.environ["GOOGLE_CLOUD_PROJECT"] = "local-project"

project_id = "local-project"
topic_id = "test-topic"
sub_id = "test-sub"

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

topic_path = publisher.topic_path(project_id, topic_id)
sub_path = subscriber.subscription_path(project_id, sub_id)
