from azure.servicebus import ServiceBusClient,ServiceBusMessage
from azure.servicebus.management import ServiceBusAdministrationClient

print("program started")
#create a ServiceBusClient object
connection_str = "Endpoint=sb://azdemoqueueallops.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=bkDxaVHrz0PwIa/a4UeT5V72PmimyS6bI+ASbLKXqsY="
servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str)
print("created service bus client")

#create a ServiceBusAdministrationClient object
servicebus_mgmt_client = ServiceBusAdministrationClient.from_connection_string(conn_str=connection_str)
print("created service bus management client object")

#create topic and subscription
topicName = "topic-01"
subName = "sub-01"
msg = ServiceBusMessage("HELLO")
max_size_in_mb = 1024

def create_topic(topic_name):
    servicebus_mgmt_client.create_topic(topic_name)
    print(f"created topic : {topic_name}")

#update topic properties
def update_topic(topic_name,max_size_in_mb):
    topic_properties = servicebus_mgmt_client.get_topic(topic_name)
    topic_properties.max_size_in_megabytes = max_size_in_mb
    servicebus_mgmt_client.update_topic(topic_properties)
    print(f"updated topic : {topic_name}")

#create subscription
def create_sub(topic_name,sub_name):
    servicebus_mgmt_client.create_subscription(topic_name,sub_name)
    print(f"created subscription : {sub_name}")


#send a message to topic
def send_msg(topic_name,message):
    sender = servicebus_client.get_topic_sender(topic_name=topic_name)
    sender.send_messages(message)
    print(f"sent message : {message}")

#receive a message from the topic
def receive_message(topic_name,sub_name):
    receiver = servicebus_client.get_subscription_receiver(topic_name,sub_name)
    received_msg = receiver.receive_messages(max_message_count=1)[0]
    print(f"received message : {received_msg}")
    receiver.complete_message(received_msg)

#delete the queue
def delete_topic(topic_name):
    servicebus_mgmt_client.delete_topic(topic_name)
    print(f"deleted topic : {topic_name}")


if __name__ == '__main__':
    create_topic(topicName)
    update_topic(topicName, max_size_in_mb)
    create_sub(topicName, subName)
    send_msg(topicName, msg)
    receive_message(topicName, subName)
    delete_topic(topicName)