from azure.servicebus import ServiceBusClient,ServiceBusMessage
from azure.servicebus.management import ServiceBusAdministrationClient

#create a ServiceBusClient object
connection_str = "Endpoint=sb://azdemoqueueallops.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=bkDxaVHrz0PwIa/a4UeT5V72PmimyS6bI+ASbLKXqsY="
servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str)

#create a ServiceBusAdministrationClient object
servicebus_mgmt_client = ServiceBusAdministrationClient.from_connection_string(conn_str=connection_str)

#create queue
queueName = "queue001"
servicebus_mgmt_client.create_queue(queueName)

#update queue properties
queue_properties = servicebus_mgmt_client.get_queue(queueName)
queue_properties.max_delivery_count = 10
servicebus_mgmt_client.update_queue(queue_properties)

#send a message to queue
sender = servicebus_client.get_queue_sender(queue_name=queueName)
msg = ServiceBusMessage("Hello World")
sender.send_messages(msg)
print(f"send message : {msg}")

#receive a message from the queue
receiver = servicebus_client.get_queue_receiver(queue_name=queueName)
received_msg = receiver.receive_messages(max_message_count=1)[0]
print(f"received message : {received_msg}")

#mark message as completed it should be delete
receiver.complete_message(received_msg)

#delete the queue
servicebus_mgmt_client.delete_queue(queueName)

print(f"deleted queue : {queueName}")