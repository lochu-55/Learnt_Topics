#include "stm32f4xx.h"
#include "stdio.h"
#include "test_uart.h"
#include "unity.h"

void USART2_config(void)
{
    // Enable UART clock and GPIO clock (PA2-Tx, PA3-Rx)
    RCC->APB1ENR |= (1 << 17);   // Enable USART2 clock
    RCC->AHB1ENR |= (1 << 0);    // Enable GPIOA clock

    // Configure PA2 (TX) and PA3 (RX) as alternate function
    GPIOA->MODER |= (2 << 4) | (2 << 6);   // Set PA2, PA3 to alternate function mode
    GPIOA->OSPEEDR |= (3 << 4) | (3 << 6); // Set PA2, PA3 to high speed
    GPIOA->AFR[0] |= (7 << 8) | (7 << 12); // Set AF7 (USART2) for PA2 and PA3

    // Enable USART by writing UE bit (13th bit) in USART_CR1 register
    USART2->CR1 = 0x00;   // Clear all control bits
    USART2->CR1 |= (1 << 13);  // Enable USART (UE)

    // Set word length to 8 data bits (M bit, 12th bit)
    USART2->CR1 &= ~(1 << 12);  // 8 data bits, set M bit to 0

    // Configure the baud rate (115200 baud with 16 MHz system clock)
    // Baud rate formula: USARTDIV = fclk / (16 * baud rate)
    // fclk = 16 MHz, baud rate = 115200
    // USARTDIV = 16,000,000 / (16 * 115200) = 8.6805556
    // Mantissa = 8, Fraction = 11 (8.6805556 - 8 = 0.6805556 -> 0.6805556 * 16 = 11)
    USART2->BRR = (8 << 4) | (11); // Set BRR register for 115200 baud rate (Mantissa = 8, Fraction = 11)

    // Enable the TX and RX by setting TE and RE bits in USART_CR1
    USART2->CR1 |= (1 << 2) | (1 << 3);  // Enable TX and RX
}

void UART_SendChar(uint8_t ch)
{
    // Write data to send in USART_DR register
    USART2->DR = ch;
    
    // Wait until the transmission is complete (TC bit is set)
    while (!(USART2->SR & (1 << 6)));  // Wait until TC (Transmission Complete) is set
    
   
}



void UART_SendString(char *str)
{
    while (*str) {
        UART_SendChar(*str++);
    }
}

// Simple delay function (if needed)
void delay(volatile uint32_t delay_time)
{
    while (delay_time--);
}



int main(void)
{
    // Configure USART2
    USART2_config();
    // Send a string over USART2
    UART_SendString(" Hello, STM32\r\n");
    while(1){
        delay(1000000);        // Add a delay if needed (adjust the number for your timing)
        UNITY_BEGIN();
        RUN_TEST(test_UART_SendChar);
        RUN_TEST(test_UART_SendString);
        UNITY_END();
    
    } 
}
