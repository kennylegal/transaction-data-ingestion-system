from kafka import KafkaConsumer
import pandas as pd
import json
if __name__ == "__main__":
    consumer = KafkaConsumer(
        'ti.public.users',
        bootstrap_servers=['localhost:29092'],
        group_id = 'User_data_consumers',
        auto_offset_reset = 'earliest'
    )

    try:
        consumer.subscribe(['ti.public.users'])
        while True:
            response = consumer.poll(timeout_ms=100)
            for topic, messages in response.items():
                for message in messages:
                    msg_text = message.value.decode("utf-8")
                    msg_dict = json.loads(msg_text)
                    msg_topic = message.topic
                    msg_offset = message.offset
                    df = pd.DataFrame([msg_dict])
                    df.to_json("data_msg.json", orient="records", lines=True)
                    print(f"This is the message: {msg_text} with offset: {msg_offset} from topic: {msg_topic}.")
    except Exception as e:
        raise e
    finally:
        consumer.close()