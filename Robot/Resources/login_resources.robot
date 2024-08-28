*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${browser}  chrome
${url}  https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F


*** Keywords ***
Opening
    open browser    ${url}      ${browser}
    maximize browser window

Login page
    go to    ${url}

Input username
    [Arguments]    ${username}
    input text    id:Email  ${username}

Input Password
    [Arguments]    ${pswd}
    input text    id:Password   ${pswd}

Login button
    click element    xpath://button[@type='submit']

Logout link
    click link    Logout

Error Message
    page should contain    Login was unsuccessful

Login success
    page should contain    Dashboard

Closing
    close all browsers

