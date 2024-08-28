*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://www.saucedemo.com/

*** Test Cases ***
Test using if else
    open browser    ${url}  ${browser}
    maximize browser window
    input text    id:user-name      standard_user
    input text    id:password       secret_sauce
    click button    xpath://input[@name='login-button']
    ${items}=   get element count    xpath://*[@class='inventory_list']/div
    log to console    ${items}

*** Keywords ***
Test1
    log to console      Found items as expected
    close browser

Test2
    log to console    Founde items less than expected
    close browser

Test3
    log to console    Exception occured
    close browser
