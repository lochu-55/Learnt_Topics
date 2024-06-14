#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include <stdio.h>

// Define a constant string as the queue name
#define QUEUE_NAME "MyQueue"

QueueHandle_t xQueue;

void vSenderTask(void *pvParameters) {
    int ivalueToSend = 0;

    for (;;) {
        // Attempt to send items to the queue
        if (xQueueSend(xQueue, &ivalueToSend, portMAX_DELAY) == pdPASS) {
            printf("Sent to %s : %d\n", QUEUE_NAME, ivalueToSend);
            ivalueToSend++;
        } else {
            printf("Failed to send to %s : %d\n", QUEUE_NAME, ivalueToSend);
        }

        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

void vReceiverTask(void *pvParameters) {
    int receivedValue;

    for (;;) {
        // Attempt to receive items from the queue
        if (xQueueReceive(xQueue, &receivedValue, portMAX_DELAY) == pdPASS) {
            printf("Received from %s : %d\n", QUEUE_NAME, receivedValue);
        } else {
            printf("Failed to receive from %s\n", QUEUE_NAME);
        }

        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

int main(void) {
    xQueue = xQueueCreate(5, sizeof(int));
    if (xQueue != NULL) {
        xTaskCreate(vSenderTask, "Sender", configMINIMAL_STACK_SIZE, NULL, 1, NULL);
        xTaskCreate(vReceiverTask, "Receiver", configMINIMAL_STACK_SIZE, NULL, 2, NULL);
        vTaskStartScheduler();
    } else {
        printf("Failed to create queue\n");
    }

    for (;;) {
    }

    return 0;
}

/*
Received from MyQueue : 0
Sent to MyQueue : 0
Sent to MyQueue : 1
Received from MyQueue : 1
Sent to MyQueue : 2
Sent to MyQueue : 3
Received from MyQueue : 2
Sent to MyQueue : 4
Sent to MyQueue : 5
Received from MyQueue : 3
Sent to MyQueue : 6
Sent to MyQueue : 7
Received from MyQueue : 4
Sent to MyQueue : 8
Sent to MyQueue : 9
Received from MyQueue : 5
Sent to MyQueue : 10
Received from MyQueue : 6
Sent to MyQueue : 11
Received from MyQueue : 7
Sent to MyQueue : 

Received from MyQueue : 8
Sent to MyQueue : 13
Received from MyQueue : 9
Sent to MyQueue : 14
Received from MyQueue : 10
Sent to MyQueue : 15

*/
