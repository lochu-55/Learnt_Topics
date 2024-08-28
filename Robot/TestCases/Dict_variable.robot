*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://www.saucedemo.com/
&{username}     a=standard_user   b=locked_out_user
...    c=problem_user    d=performance_glitch_user
...    e=error_user   f=visual_user

*** Test Cases ***
Test Dict variable
    open browser    ${url}  ${browser}
    maximize browser window
    set selenium speed    1
    input text    id:user-name      ${username}[c]
    input text    id:password       secret_sauce
    click button    xpath://input[@name='login-button']
    ${items}=   get element count    xpath://*[@class='inventory_list']/div
    log to console    ${items}

*** Keywords ***

