*** Settings ***
Library     SeleniumLibrary
Variables    ../PageObjects/Locator.py
*** Keywords ***
Open_my_browser
    [Arguments]    ${url}   ${browser}
    open browser    ${url}  ${browser}
    maximize browser window

Enter username
    [Arguments]    ${user}
    Input text      ${txt_loginuser}    ${user}

Enter password
    [Arguments]    ${pswd}
    Input text      ${txt_loginpassword}    ${pswd}

Click SignIn
    click button    ${loginbtn}

Successful login
    title should be     Login: Mercury Tours

Closing
    close all browsers

