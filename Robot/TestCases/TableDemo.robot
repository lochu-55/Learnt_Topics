*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
Table
    set selenium speed    0.5
    open browser    ${url}    ${browser}
    maximize browser window
    ${row}=  get element count    xpath://table[@name='BookTable']/tbody/tr
    log to console    ${row}
    ${col}=  get element count    xpath://table[@name='BookTable']/tbody/tr[1]/th
    log to console    ${col}
    ${data}=    get text    xpath://table[@name='BookTable']/tbody/tr[4]/td[1]
    log to console    ${data}

    table column should contain     xpath://table[@name='BookTable']    2   Author
    table row should contain    xpath://table[@name='BookTable']    4   Learn JS
    table cell should contain   xpath://table[@name='BookTable']    5   2    Mukesh
    table header should contain    xpath://table[@name='BookTable']     BookName
    #table footer should contain    xpath://table[@name='BookTable']     `Amit
    table should contain    xpath://table[@name='BookTable']    Price

    close browser