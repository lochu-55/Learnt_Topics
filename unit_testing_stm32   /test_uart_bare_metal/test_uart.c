#include "unity.h"
#include "uart.h"
#include "stm32f4xx.h"


extern void USART2_config(void);
extern void UART_SendChar(uint8_t ch);
extern void UART_SendString(char *str);
extern uint8_t UART_ReceiveChar(void);
extern void delay(void);


void setUp(void) {
    // Setup code, called before each test
}

void tearDown(void) {
    // Tear down code, called after each test
}

void test_USART2_config(void) {
    USART2_config();
    TEST_ASSERT_TRUE(RCC->APB1ENR & (1 << 17));  // Check if USART2 clock is enabled
    TEST_ASSERT_TRUE(RCC->AHB1ENR & (1 << 0));   // Check if GPIOA clock is enabled
    TEST_ASSERT_TRUE(GPIOA->MODER & (2 << 4));    // PA2 should be in alternate function mode
    TEST_ASSERT_TRUE(GPIOA->MODER & (2 << 6));    // PA3 should be in alternate function mode
    TEST_ASSERT_EQUAL(USART2->BRR, (8 << 4) | 11); // BRR register for 115200 baud
}

void test_UART_SendChar(void) {
    UART_SendChar('A');
   
}

void test_UART_SendString(void) {
    UART_SendString("\nstm32\r\n");
}


void test_delay(void) {
    delay();
    TEST_PASS();
}


