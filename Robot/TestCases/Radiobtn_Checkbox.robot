*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Register.html


*** Test Cases ***
Testing Radio Btns and Check Boxes
    open browser    ${url}    ${browser}
    maximize browser window
    set selenium speed    0.5
    title should be     Register

    select radio button     radiooptions   FeMale
    select checkbox    id:checkbox3
    select checkbox    id:checkbox1
    unselect checkbox   id:checkbox3

    close browser



*** Keywords ***
