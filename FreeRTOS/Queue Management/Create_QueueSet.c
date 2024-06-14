#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include <stdio.h>
#include <stdarg.h>

#define QUEUE_LENGTH_1 3
#define QUEUE_LENGTH_2 4

#define ITEM_SIZE_1 sizeof(uint32_t)
#define ITEM_SIZE_2 sizeof(uint32_t)
#define COMBINED_LENGTH (QUEUE_LENGTH_1 + QUEUE_LENGTH_2)

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

void vProcessValueFromQueue1(uint32_t value) {

    vPrintString("Value received from Queue 1: %u\n", value);
}

void vProcessValueFromQueue2(uint32_t value) {

    vPrintString("Value received from Queue 2: %u\n", value);
}

void vSenderTask(void *pvParameters) {
    QueueHandle_t xQueue1 = ((QueueHandle_t *)pvParameters)[0];
    QueueHandle_t xQueue2 = ((QueueHandle_t *)pvParameters)[1];
    uint32_t valueToSend = 0;
    
    while (1) {
        valueToSend++;
        if (xQueueSend(xQueue1, &valueToSend, 0) != pdPASS) {
            vPrintString("Failed to send to Queue 1\n");
        }
        
        valueToSend++;
        if (xQueueSend(xQueue2, &valueToSend, 0) != pdPASS) {
            vPrintString("Failed to send to Queue 2\n");
        }
        
        vTaskDelay(pdMS_TO_TICKS(1000)); // Delay for 1 second
    }
}

void vReceiverTask(void *pvParameters) {
    static QueueSetHandle_t xQueueSet;
    QueueHandle_t xQueue1 = ((QueueHandle_t *)pvParameters)[0];
    QueueHandle_t xQueue2 = ((QueueHandle_t *)pvParameters)[1];
    QueueSetMemberHandle_t xActivatedMember;
    uint32_t xReceivedFromQueue1;
    uint32_t xReceivedFromQueue2;
    
    xQueueSet = xQueueCreateSet(COMBINED_LENGTH);
    xQueueAddToSet(xQueue1, xQueueSet);
    xQueueAddToSet(xQueue2, xQueueSet);
    
    for (;;) {
        xActivatedMember = xQueueSelectFromSet(xQueueSet, pdMS_TO_TICKS(200));
        
        if (xActivatedMember == xQueue1) {
            xQueueReceive(xActivatedMember, &xReceivedFromQueue1, 0);
            vProcessValueFromQueue1(xReceivedFromQueue1);
        } else if (xActivatedMember == xQueue2) {
            xQueueReceive(xActivatedMember, &xReceivedFromQueue2, 0);
            vProcessValueFromQueue2(xReceivedFromQueue2);
        } else {
            vPrintString("The 200ms block time expired without an RTOS queue being ready to process\n");
        }
    }
}

int main(void) {
    static QueueHandle_t xQueue1, xQueue2;
    static QueueHandle_t queues[2];
    
    xQueue1 = xQueueCreate(QUEUE_LENGTH_1, ITEM_SIZE_1);
    xQueue2 = xQueueCreate(QUEUE_LENGTH_2, ITEM_SIZE_2);
    
    if (xQueue1 == NULL || xQueue2 == NULL) {
        vPrintString("Failed to create queues\n");
        return 1;
    }
    
    queues[0] = xQueue1;
    queues[1] = xQueue2;
    
    xTaskCreate(vSenderTask, "SenderTask", configMINIMAL_STACK_SIZE, queues, 1, NULL);
    xTaskCreate(vReceiverTask, "ReceiverTask", configMINIMAL_STACK_SIZE, queues, 1, NULL);
    
    vTaskStartScheduler();
    
    for (;;);
}

