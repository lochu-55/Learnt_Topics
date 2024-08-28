*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Windows.html
${url1}     https://www.selenium.dev/

*** Test Cases ***
Navigation through windows
    set selenium speed    0.5
    open browser    ${url}    ${browser}
    maximize browser window
    ${loc}  get location
    log to console    ${loc}

    go to    ${url1}
    ${loc}  get location
    log to console    ${loc}

    go back
    ${loc}  get location
    log to console    ${loc}


    close browser

*** Keywords ***
