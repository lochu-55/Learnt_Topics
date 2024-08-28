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

void vSenderTask(void *pvvar) {
    int ivalueToSend;
    
    for(;;) {
        ivalueToSend = 1;
        if (xQueueSend(xQueue, &ivalueToSend, pdMS_TO_TICKS(100)) == pdPASS) 
        {
            vPrintString("Sent : %d\n", ivalueToSend);
        }
        else
        {
            vPrintString("Queue is full. Failed to send : %d\n", ivalueToSend);
        }
        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

void vReceiverTask(void *pvvar) {
    int iReceivedValue;
    
    for(;;) {

        if (xQueueReceive(xQueue, &iReceivedValue, pdMS_TO_TICKS(100)) == pdPASS) 
        {
            vPrintString("Received : %d\n", iReceivedValue);
        }
        else
        {
            vPrintString("Queue is empty. No data received \n");
        }
        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

void vDeleteTask(void *pvvar) {
    for(;;) {
        vPrintString("After Deleting the queue \n");
        vQueueDelete(xQueue);
    }
}

int main(void) {
    xQueue = xQueueCreate(5, sizeof(int));
    if (xQueue != NULL) {
        vPrintString("Queue can be created\n");
        xTaskCreate(vSenderTask, "sender",130,NULL,1,NULL);
        xTaskCreate(vReceiverTask, "Receiver",130,NULL,1,NULL);
        xTaskCreate(vDeleteTask, "Deleting",130,NULL,1,NULL);
        vTaskStartScheduler();
       
    }
    else {
        vPrintString("The queue can not be created\n");
    }
    for(;;) {
    }
}

/*
Queue can be created
After Deleting the queue 
*/
    
