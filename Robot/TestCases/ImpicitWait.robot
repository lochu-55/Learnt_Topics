*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Register.html


*** Test Cases ***
Testing Speed
    open browser    ${url}    ${browser}
    maximize browser window

    ${time} =    get selenium implicit wait
    log to console    ${time}


    set selenium implicit wait    2 seconds

    ${time} =    get selenium implicit wait
    log to console    ${time}
    LoginProcess
    close browser



*** Keywords ***
LoginProcess
    input text  xpath://input[@placeholder='First Name1']    Lochani
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