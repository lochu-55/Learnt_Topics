*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/POM_keywords.robot


*** Variables ***
${browser}  headlesschrome
${siteURL}  https://demo.guru99.com/test/newtours/
${user}     tutorial
${pwd}      tutorial


*** Test Cases ***
Login Test
    set selenium speed  0.5
    Open_my_browser     ${siteURL}   ${browser}
    Enter username  ${user}
    Enter password  ${pwd}
    Click SignIn
    sleep   3
    Successful login
    Closing