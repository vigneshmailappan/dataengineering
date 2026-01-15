
from google.cloud import pubsub_v1

project_id = "local-project"
sub_id = "test-sub"

subscriber = pubsub_v1.SubscriberClient()
sub_path = subscriber.subscription_path(project_id, sub_id)

resp = subscriber.pull(
    request={"subscription": sub_path, "max_messages": 10},
    timeout=5,
)

if not resp.received_messages:
    print("📭 No messages found.")
else:
    for m in resp.received_messages:
        print(m.message.data.decode("utf-8", errors="replace"))
    subscriber.acknowledge(
        request={"subscription": sub_path, "ack_ids": [m.ack_id for m in resp.received_messages]}
    )
    print("✅ Acked.")
