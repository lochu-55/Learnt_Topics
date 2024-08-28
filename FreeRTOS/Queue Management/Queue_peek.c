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
            if (xQueueSendToBack(xQueue, &ivalueToSend, pdMS_TO_TICKS(100)) == pdPASS) 
            {

               vPrintString("Sent : %d\n", ivalueToSend);

            }
            else
            {

                
                vPrintString("Queue is full. Failed to send : %d\n", ivalueToSend);

            }
            
            uxNumberOfItems = uxQueueMessagesWaiting(xQueue);

            vPrintString("number of items in a queue %d\n",uxNumberOfItems);

            vTaskDelay(pdMS_TO_TICKS(500));
        }

    }
}

void vPeekTask (void *pvar) {
    int i;
    if (xQueue != 0) {
        if ( xQueuePeek(xQueue, &i, 100) == pdPASS) {
            taskENTER_CRITICAL();
            vPrintString("Peek value : %d\n",i);
            taskEXIT_CRITICAL();
        }
    }
    else {
        vPrintString("the queue could not be created\n");
    }
    for(;;) {
        
    }
}

int main(void) {
    xQueue = xQueueCreate(5, sizeof(int));
    if (xQueue != NULL) {
        xTaskCreate(vSenderTask, "sender",130,NULL,1,NULL);
        xTaskCreate(vPeekTask, "peek",130,NULL,1,NULL);
        vTaskStartScheduler();
    }
    else {
        printf("Queue creation failed\n");
    }
    for(;;) {
    }
}
