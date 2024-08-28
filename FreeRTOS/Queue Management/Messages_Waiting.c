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

void vSenderTask(void *pvvar)  {
    UBaseType_t uxNumberOfItems;
    int ivalueToSend;
    
    for(;;) {
        for (int i = 0 ; i < 5; i++) {
            ivalueToSend = i;
            if (xQueueSend(xQueue, &ivalueToSend, pdMS_TO_TICKS(100)) == pdPASS) 
            {
               taskENTER_CRITICAL();

               vPrintString("Sent : %d\n", ivalueToSend);
               taskEXIT_CRITICAL();

            }
            else
            {
                taskENTER_CRITICAL();

                
                vPrintString("Queue is full. Failed to send : %d\n", ivalueToSend);
                taskEXIT_CRITICAL();

            }
            
            uxNumberOfItems = uxQueueMessagesWaiting(xQueue);
            taskENTER_CRITICAL();

            vPrintString("number of items in a queue %d\n",uxNumberOfItems);
            taskEXIT_CRITICAL();

            vTaskDelay(pdMS_TO_TICKS(500));
        }

    }
}



int main(void) {
    xQueue = xQueueCreate(5, sizeof(int));
    if (xQueue != NULL) {
        
        xTaskCreate(vSenderTask, "sender",130,NULL,1,NULL);
        vTaskStartScheduler();
    }
    else {
        printf("Queue creation failed\n");
    }
    for(;;) {
    }
}

/*
Sent : 0
number of items in a queue 1
Sent : 1
number of items in a queue 2
Sent : 2
number of items in a queue 3
Sent : 3
number of items in a queue 4
Sent : 4
number of items in a queue 5
Queue is full. Failed to send : 0
number of items in a queue 5
Queue is full. Failed to send : 1
number of items in a queue 5
Queue is full. Failed to send : 2
number of items in a queue 5
Queue is full. Failed to send : 3
number of items in a queue 5
Queue is full. Failed to send : 4
number of items in a queue 5
Queue is full. Failed to send : 0
number of items in a queue 5
*/
    
