*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Windows.html


*** Test Cases ***
Tabbed Windows
    open browser    ${url}    ${browser}
    maximize browser window
    set selenium speed    0.5
    click element    xpath://*[@id="Tabbed"]/a/button
    Switch Window    title=Selenium
    click element    xpath://a[@href='/downloads']
    sleep   2
    close all browsers

*** Keywords ***
