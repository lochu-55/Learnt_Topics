from azure.servicebus import ServiceBusClient,ServiceBusMessage

connection_str = "Endpoint=sb://azdemotopic.servicebus.windows.net/;SharedAccessKeyName=TopicBus;SharedAccessKey=4hL5rhbn5FDQeLUWnaqSVfaMXgkxX8B5F+ASbFJuxO0=;EntityPath=topic001"

topicName = "topic001"

def send_message():
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str)

    with servicebus_client:
        sender = servicebus_client.get_topic_sender(topic_name=topicName)
        with sender:
            batch_msg = sender.create_message_batch()
            for i in range(10):
                try:
                    msg = ServiceBusMessage("Message no. {}".format(i))
                    batch_msg.add_message(msg)
                except ValueError:
                    #batch has reached its size limit
                    break
            sender.send_messages(batch_msg)
            print("sent a batch of 10 messages")


if __name__ == '__main__':
    send_message()
