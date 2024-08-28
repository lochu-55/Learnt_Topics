*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://www.saucedemo.com/
@{username}     standard_user   locked_out_user
...    problem_user    performance_glitch_user
...    error_user   visual_user

*** Test Cases ***
Test List variable
    open browser    ${url}  ${browser}
    maximize browser window
    set selenium speed    1
    input text    id:user-name      ${username}[3]
    input text    id:password       secret_sauce
    click button    xpath://input[@name='login-button']
    ${items}=   get element count    xpath://*[@class='inventory_list']/div
    log to console    ${items}

*** Keywords ***

