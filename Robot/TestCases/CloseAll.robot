*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Register.html
${url1}  https://techcanvass.com/Examples/multi-select.html

*** Test Cases ***
Testing Speed
    open browser    ${url}    ${browser}
    maximize browser window

    open browser    ${url1}     ${browser}
    maximize browser window

    close all browsers