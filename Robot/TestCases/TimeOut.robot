*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Register.html


*** Test Cases ***
Testing Speed
    open browser    ${url}    ${browser}
    maximize browser window

    ${time} =    get selenium timeout
    log to console    ${time}


    set selenium timeout    2 seconds
    wait until page contains    Registration

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


