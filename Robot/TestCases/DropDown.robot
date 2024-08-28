*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Register.html


*** Test Cases ***
Testing DropDown
    open browser    ${url}    ${browser}
    maximize browser window
    title should be     Register
    LoginToApp
    close browser



*** Keywords ***
LoginToApp
    select from list by label   Skills  Adobe InDesign
    sleep    2
    select from list by index   Skills  15
    sleep    3
    select from list by value   Skills  HTML
    sleep    3
