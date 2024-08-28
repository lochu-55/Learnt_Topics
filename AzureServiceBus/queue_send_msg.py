from azure.servicebus import ServiceBusClient,ServiceBusMessage

connection_str = "Endpoint=sb://azdemoservicebus.servicebus.windows.net/;SharedAccessKeyName=ConnectedStrings;SharedAccessKey=367pwFZH1eKk9qSe32mUq7TPQhExkCPeH+ASbCrk/sQ=;EntityPath=firstqueue"

queueName = "firstqueue"

def send_message(connection_str,queueName):
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str)
    sender = servicebus_client.get_queue_sender(queue_name=queueName)
    msg = ServiceBusMessage("Hello World 002")
    sender.send_messages(msg)
    sender.close()
    servicebus_client.close()
    return "message sent successfully"

if __name__ == '__main__':
    res = send_message(connection_str,queueName)
    print(res)