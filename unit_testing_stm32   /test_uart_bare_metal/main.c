// stm32f4xx.c
#include "stm32f4xx.h"
#
// Mock variables to simulate hardware interactions
volatile uint8_t mock_usart_dr = 0;   // Simulates USART Data Register (DR)
volatile uint32_t mock_usart_sr = 0;  // Simulates USART Status Register (SR)


// Function to send a character
void UART_SendChar(uint8_t ch)
{
    // Simulate the USART data register write operation
    mock_usart_dr = ch;
    
    // Simulate the USART status flags
    mock_usart_sr |= USART_SR_TXE;  // Indicate that TXE flag is set
    while (!(mock_usart_sr & USART_SR_TC)) {
        // Simulate waiting for transmission complete
    }
    mock_usart_sr &= ~USART_SR_TC;  // Clear the TC flag after transmission is complete
}
