# check_messages.py

import pubsub_emulate as pse

# Pull up to 10 messages from the subscription
response = pse.subscriber.pull(
    request={
        "subscription": pse.sub_path,
        "max_messages": 10,
    },
    timeout=5,
)

# Print results
if not response.received_messages:
    print("📭 No messages found in subscription.")
else:
    print(f"📨 Found {len(response.received_messages)} message(s):")
    for msg in response.received_messages:
        print("Data:", msg.message.data.decode())
        print("Attributes:", msg.message.attributes)
        print("---")

    # Acknowledge messages
    ack_ids = [m.ack_id for m in response.received_messages]
    pse.subscriber.acknowledge(
        request={
            "subscription": pse.sub_path,
            "ack_ids": ack_ids,
        }
    )
    print("✅ Messages acknowledged.")