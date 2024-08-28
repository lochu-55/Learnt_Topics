*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Alerts.html


*** Test Cases ***
Handling Alerts
    open browser    ${url}    ${browser}
    maximize browser window
    set selenium speed    1
    click element    xpath://a[@href='#CancelTab']
    click element   xpath://button[@class='btn btn-primary']
    #handle alert    accept
    #handle alert    dismiss
    handle alert    leave
    alert should be present    Press a Button !
*** Keywords ***
