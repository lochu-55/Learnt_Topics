<<<<<<< HEAD
#include "stm32f4xx.h"
#include "FreeRTOS.h"
#include "FreeRTOSConfig.h"
#include "task.h"
extern void xPortSysTickHandler( void );

void delay (uint32_t millisec)
{
  TickType_t ticks = millisec / portTICK_PERIOD_MS;
  
  vTaskDelay(ticks ? ticks : 1);          /* Minimum delay = 1 tick */
  
}

/**
* @brief This function handles System tick timer.
*/
void SysTick_Handler(void)
{
    //uwTick++;
    xPortSysTickHandler();
}
=======

#include "stm32f4xx.h"
#include "FreeRTOS.h"
#include "FreeRTOSConfig.h"
#include "task.h"
extern void xPortSysTickHandler( void );

void delay (uint32_t millisec)
{
  TickType_t ticks = millisec / portTICK_PERIOD_MS;
  
  vTaskDelay(ticks ? ticks : 1);          /* Minimum delay = 1 tick */
  
}

/**
* @brief This function handles System tick timer.
*/
void SysTick_Handler(void)
{
    //uwTick++;
    xPortSysTickHandler();
}
>>>>>>> 6ddf5bfaa9da0da3c93a81a016f451a9a91e29b9
