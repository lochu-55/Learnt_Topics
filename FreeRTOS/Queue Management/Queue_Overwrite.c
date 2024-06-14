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
    UBaseType_t uxNumberOfItems;
    int ivalueToSend;
    int j = 10;

    for (;;) {
        for (int i = 0; i < 5; i++) {
            ivalueToSend = i;

            if (i == 3) {
                taskENTER_CRITICAL();
                if (xQueueOverwrite(xQueue, &j) == pdPASS) {
                    vPrintString("Queue overwritten with : %d\n", j);

                } else {
                    vPrintString("Failed to overwrite queue.\n");
                }
                taskEXIT_CRITICAL();
            } else {
                if (xQueueSend(xQueue, &ivalueToSend, pdMS_TO_TICKS(100)) == pdPASS) {
                    vPrintString("Sent : %d\n", ivalueToSend);
                } else {
                    vPrintString("Queue is full. Failed to send : %d\n", ivalueToSend);
                }
            }

            uxNumberOfItems = uxQueueMessagesWaiting(xQueue);
            vPrintString("Number of items in the queue: %d\n", uxNumberOfItems);

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
