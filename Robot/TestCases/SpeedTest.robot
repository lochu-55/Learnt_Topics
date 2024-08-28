*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Register.html


*** Test Cases ***
Testing Speed
    ${speed} =  get selenium speed
    log to console    ${speed}

    open browser    ${url}    ${browser}
    maximize browser window
    title should be     hello
    set selenium speed    0.5
    LoginProcess
    close browser



*** Keywords ***
LoginProcess
    input text  xpath://input[@placeholder='First Name']    Lochani
    input text  xpath://input[@placeholder='Last Name']    Vilehya
    input text  xpath://input[@type='email']    lochu5vilehya@gmail.com
    input text  xpath://input[@type='tel']  8341130962

    select radio button     radiooptions   FeMale
    select checkbox    id:checkbox3
    select checkbox    id:checkbox1
    unselect checkbox   id:checkbox3
    select from list by label   Skills  Adobe InDesign
    select from list by index   Skills  15
    select from list by value   Skills  HTML

    ${speed} =  get selenium speed
    log to console    ${speed}
