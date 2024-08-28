from azure.servicebus import ServiceBusClient,ServiceBusMessage

connection_str = "Endpoint=sb://azdemoservicebus.servicebus.windows.net/;SharedAccessKeyName=ConnectedStrings;SharedAccessKey=367pwFZH1eKk9qSe32mUq7TPQhExkCPeH+ASbCrk/sQ=;EntityPath=firstqueue"

queueName = "firstqueue"

def receive_msg(connection_str,queueName):
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str)
    receiver = servicebus_client.get_queue_receiver(queue_name=queueName)

    with receiver:
        for msg in receiver:
            print(msg)
            #receiver.complete_message(msg)
    servicebus_client.close()

if __name__ == '__main__':
   receive_msg(connection_str,queueName)
