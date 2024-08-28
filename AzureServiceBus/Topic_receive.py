from azure.servicebus import ServiceBusClient,ServiceBusMessage

connection_str = "Endpoint=sb://azdemotopic.servicebus.windows.net/;SharedAccessKeyName=TopicBus;SharedAccessKey=4hL5rhbn5FDQeLUWnaqSVfaMXgkxX8B5F+ASbFJuxO0=;EntityPath=topic001"

topicName = "topic001"
subName = "sub001"
def receive_msg(connection_str,topicName,subName):
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str)
    receiver = servicebus_client.get_subscription_receiver(topic_name=topicName,subscription_name=subName)
    with receiver:
        for msg in receiver:
            print(msg)
            receiver.complete_message(msg)

    servicebus_client.close()

if __name__ == '__main__':
   receive_msg(connection_str,topicName,subName)
