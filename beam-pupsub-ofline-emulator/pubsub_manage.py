import argparse
import pubsub_emulate as pse

parser = argparse.ArgumentParser(description="Pub/Sub local manager")
parser.add_argument("--action", type=str, help="input your action (1 -> delete)")
args = parser.parse_args()
print("Action:", args.action)

if args.action == '1':
    try:
        # Check if topic exists
        pse.publisher.get_topic(request={"topic": pse.topic_path})
        print(f"Topic exists: {pse.topic_path}")

        # List subscriptions for the topic
        subscriptions = list(pse.publisher.list_topic_subscriptions(request={"topic": pse.topic_path}))

        if subscriptions:
            for sub in subscriptions:
                try:
                    pse.subscriber.delete_subscription(request={"subscription": sub})
                    print(f"Deleted subscription: {sub}")
                except Exception as e:
                    print(f"Failed to delete subscription {sub}: {e}")
            print("All subscriptions deleted")
        else:
            print("No subscriptions to delete")

        # Delete the topic
        try:
            pse.publisher.delete_topic(request={"topic": pse.topic_path})
            print(f"Topic deleted: {pse.topic_path}")
        except Exception as e:
            print(f"Failed to delete topic: {e}")

    except Exception:
        print(f"Topic not found: {pse.topic_path}")
