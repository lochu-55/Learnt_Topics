*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Windows.html
${url1}     https://www.selenium.dev/

*** Test Cases ***
Tabbed Windows
    set selenium speed    0.5
    open browser    ${url}    ${browser}
    maximize browser window

    open browser    ${url1}    ${browser}
    maximize browser window

    switch browser    1
    ${log1}     get title
    log to console    ${log1}

    switch browser    2
    ${log2}     get title
    log to console    ${log2}


    close all browsers
