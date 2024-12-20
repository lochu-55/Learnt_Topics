#include "main.h"
#include "FreeRTOS.h"
#include "task.h"
#include "unity.h"

// Declare the required functions (from CubeMX generated code)
void SystemClock_Config(void);
void MX_GPIO_Init(void);
void MX_USART2_UART_Init(void);

UART_HandleTypeDef huart2; // UART handle for USART2

/* UART driver functions */
void uart_driver_init(void);
void uart_driver_send(uint8_t data);

/* UART Test Functions */
void test_uart_driver_send(void);  // Declare the test function

/* Unity Test Functions */
void test_uart_driver_send_task(void *pvParameters);

/* Function prototypes */
int _write(int file, char *ptr, int len);  // For redirecting printf

void setUp(void) {
    // Initialization before each test, if required
}

void tearDown(void) {
    // Clean-up after each test, if required
}

/* Main function to initialize system and run tests */
int main(void) {
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_USART2_UART_Init();

    // Initialize the UART driver
    uart_driver_init();

    // Unity test setup
    UNITY_BEGIN();

    // Create FreeRTOS task to send data continuously
    xTaskCreate(test_uart_driver_send_task, "SendTask", 128, NULL, 1, NULL);

    // Run the Unity tests
    RUN_TEST(uart_driver_send);
    RUN_TEST(test_uart_driver_send);

    UNITY_END();

    // Start the FreeRTOS scheduler
    vTaskStartScheduler();

    while (1) {
        // The main loop should not be reached if the scheduler is running
    }
}

/* UART Driver Initialization */
void uart_driver_init(void) {
    HAL_UART_Init(&huart2);
}

/* UART Send Function */
void uart_driver_send(uint8_t data) {
	HAL_StatusTypeDef status = HAL_UART_Transmit(&huart2, &data, 1, HAL_MAX_DELAY);
	TEST_ASSERT_EQUAL(HAL_OK, status);
    printf("Sent data: %c %d\n", data,data);  // Print sent data to the ITM console for debugging
}

/* Task to Continuously Send Data */
void test_uart_driver_send_task(void *pvParameters) {
    uint8_t testByte = 'A';  // Data to send

    while (1) {

        uart_driver_send(testByte);  // Send data continuously
        testByte++;  // Increment the byte (you can modify this for different data)

        // Simulate a small delay before sending the next byte
        vTaskDelay(pdMS_TO_TICKS(100));  // Delay for 100 ms before sending again
    }
}

/* Unity Test for UART Send */
void test_uart_driver_send(void) {
    uint8_t testByte = 'A'; // Data to send
    uart_driver_send(testByte);  // Call the function to send data
}

/* Redirect printf to ITM Console */
int _write(int file, char *ptr, int len) {
    for (int i = 0; i < len; i++) {
        ITM_SendChar(*ptr++);
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

void MX_GPIO_Init(void) {
    // GPIO Initialization (CubeMX generated code)
}

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
