from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Connection string to your Service Bus namespace
connection_str = "Endpoint=sb://azdemoservicebus.servicebus.windows.net/;SharedAccessKeyName=ConnectedStrings;SharedAccessKey=367pwFZH1eKk9qSe32mUq7TPQhExkCPeH+ASbCrk/sQ=;EntityPath=firstqueue"

queueName = "firstqueue"

# Number of messages to delete (adjust as needed)
num_messages_to_delete = 2

# Create a ServiceBusClient instance
servicebus_client = ServiceBusClient.from_connection_string(connection_str)

# Create a ServiceBusReceiver for the queue
receiver = servicebus_client.get_queue_receiver(queueName)

# Receive and delete messages from the queue
with receiver:
    messages = receiver.receive_messages(max_message_count=num_messages_to_delete)
    for message in messages:
        print("Deleting message:", message)
        receiver.complete_message(message)

print("Messages deleted successfully.")
