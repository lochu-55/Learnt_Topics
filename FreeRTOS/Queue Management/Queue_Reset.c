#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include <stdio.h>
#include <stdarg.h>

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

QueueHandle_t xQueue;

void vSenderTask(void *pvParameters) {
    int ivalueToSend = 0;
    UBaseType_t uxNumberOfItems;

    for (;;) {
        // Attempt to send items to the queue
        if (xQueueSend(xQueue, &ivalueToSend, portMAX_DELAY) == pdPASS) {
            if (ivalueToSend == 3) {
            // Reset the queue after sending 3 items
            xQueueReset(xQueue);
            printf("Queue reset\n");
        }
            printf("Sent : %d\n", ivalueToSend);
            ivalueToSend++;
        } else {
            printf("Failed to send : %d\n", ivalueToSend);
        }

        
 uxNumberOfItems = uxQueueMessagesWaiting(xQueue);

            vPrintString("number of items in a queue %d\n",uxNumberOfItems);

        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

void vReceiverTask(void *pvParameters) {
    int receivedValue;

    for (;;) {
        // Attempt to receive items from the queue
        if (xQueueReceive(xQueue, &receivedValue, portMAX_DELAY) == pdPASS) {
            printf("Received : %d\n", receivedValue);
        } else {
            printf("Failed to receive\n");
        }

        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}


int main(void) {
    xQueue = xQueueCreate(5, sizeof(int));
    if (xQueue != NULL) {
        xTaskCreate(vSenderTask, "sender",130,NULL,1,NULL);
        xTaskCreate(vReceiverTask, "Receiver", configMINIMAL_STACK_SIZE, NULL, 1, NULL);        
        vTaskStartScheduler();
    }
    else {
        printf("Queue creation failed\n");
    }
    for(;;) {
    }
}

/*
Sent : Received 0 numb:iteer of items in a queue 0
Sent : 1
number of items in a queue 1
Received : 1
Sent : 2
number of items in a queue 1
Queue reset
Sent : 3
number of items in a queue 0
Sent : 4Received
number  ite of items in a queue 0
Sent : 5
number of items in a queue 1
Received : 5
Sent : 6
number of items in a queue 1
Sent : 7
number of items in a queue 2
Received : 6
Sent : 8
number of items in a queue 2
Sent : 9
number of items in a queue 3
Received : 7
Sent : 10
number of items in a queue 3
Sent : 11
number of items in a queue 4
Received : 8
Sent : 12
number of items in a queue 4
Sent : 13
number of items in a queue 5
Received : 9
Sent : 14
number of items in a queue 5
ReceiveSent : 1d5
 10
5
number of items in a queue 5
ReceivedSent : 1 
 11
6
number of items in a queue 5


*/