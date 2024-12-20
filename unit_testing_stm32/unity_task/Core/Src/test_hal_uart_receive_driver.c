#include "main.h"
#include "FreeRTOS.h"
#include "task.h"
#include "unity.h"
#include "stdio.h"

// UART handle for USART2
UART_HandleTypeDef huart2;

/* UART driver functions */
void uart_driver_init(void);
void uart_driver_receive(void);

void SystemClock_Config(void);
void MX_USART2_UART_Init(void);

int _write(int file, char *ptr, int len);  // For redirecting printf

/* Unity Test Setup */
void setUp(void) {
    HAL_Init();
    SystemClock_Config();
    MX_USART2_UART_Init();
    uart_driver_init();
}

void tearDown(void) {
    // Clean-up after each test, if required
}

/* UART Driver Initialization */
void uart_driver_init(void) {
    if (HAL_UART_Init(&huart2) != HAL_OK) {
        Error_Handler();
    }
}

/* UART Receive Function to receive a string */
void uart_driver_receive(void) {
    uint8_t receivedByte;
    uint8_t buffer[100];  // Buffer to store received string
    uint16_t index = 0;

    // Receive data byte-by-byte until newline or carriage return is encountered
    while (1) {
        HAL_StatusTypeDef status = HAL_UART_Receive(&huart2, &receivedByte, 1, HAL_MAX_DELAY);

        if (status == HAL_OK) {
            // Store received byte in buffer
            if (receivedByte == '\n' || receivedByte == '\r') {  // Newline or carriage return as delimiter
                buffer[index] = '\0';  // Null-terminate the string
                printf("Received string: %s\n", buffer);
                return;
            }
            buffer[index++] = receivedByte;
            if (index >= sizeof(buffer) - 1) {
                buffer[index] = '\0';  // Ensure null-termination if buffer is full
                printf("Buffer overflow\n");
                return;
            }
        } else {
            printf("UART Receive Error: %lu\n", huart2.ErrorCode);
        }
    }
}

/* Test Case for UART Receive Function */
void test_uart_driver_receive(void) {
    printf(" Please send a string via UART to test UART reception...\n");
    uart_driver_receive();  // Call the function and wait for input
    TEST_PASS_MESSAGE("UART reception test complete. Verify received string in the console output.");
}

/* Redirect printf to ITM Console or UART */
int _write(int file, char *ptr, int len) {
    for (int i = 0; i < len; i++) {
        ITM_SendChar(*ptr++);  // Send data to ITM console
    }
    return len;
}

/* System Clock Configuration */
void SystemClock_Config(void) {
    // System Clock Configuration (CubeMX generated code)
    RCC_OscInitTypeDef RCC_OscInitStruct = {0};
    RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

    __HAL_RCC_PWR_CLK_ENABLE();
    __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE2);

    RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
    RCC_OscInitStruct.HSIState = RCC_HSI_ON;
    RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
    RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
    RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
    RCC_OscInitStruct.PLL.PLLM = 16;
    RCC_OscInitStruct.PLL.PLLN = 336;
    RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV4;
    RCC_OscInitStruct.PLL.PLLQ = 7;
    if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK) {
        Error_Handler();
    }

    RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_SYSCLK |
                                  RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;
    RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
    RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
    RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
    RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

    if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK) {
        Error_Handler();
    }
}

/* USART2 UART Initialization */
void MX_USART2_UART_Init(void) {
    huart2.Instance = USART2;
    huart2.Init.BaudRate = 115200;
    huart2.Init.WordLength = UART_WORDLENGTH_8B;
    huart2.Init.StopBits = UART_STOPBITS_1;
    huart2.Init.Parity = UART_PARITY_NONE;
    huart2.Init.Mode = UART_MODE_TX_RX;
    huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
    huart2.Init.OverSampling = UART_OVERSAMPLING_16;
    if (HAL_UART_Init(&huart2) != HAL_OK) {
        Error_Handler();
    }
}

void Error_Handler(void) {
    __disable_irq();
    while (1) {
        // Infinite loop for error handling
    }
}

/* Main Function */
int main(void) {
    UNITY_BEGIN();

    RUN_TEST(test_uart_driver_receive);

    UNITY_END();

    while (1) {
        // The main loop should not be reached if tests are running
    }
}
