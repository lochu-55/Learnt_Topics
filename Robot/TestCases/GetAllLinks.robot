*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.guru99.com/test/newtours/
*** Test Cases ***
Get Links
    set selenium speed    0.5
    open browser    ${url}    ${browser}
    maximize browser window
    ${countLinks}=  get element count    xpath://a
    log to console    ${countLinks}


    @{linkItems}    create list
    FOR    ${i}     IN RANGE   1     ${countLinks}+1
    ${linkText}=    get text    xpath:(//a)[${i}]
    log to console  ${linkText}
    END

    close browser