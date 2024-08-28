*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
LoginBrowser
    [Arguments]    ${appurl}    ${appbrowser}
    set selenium speed    0.5
    open browser    ${appurl}    ${appbrowser}
    maximize browser window
    ${title}=   get title
    [Return]    ${title}