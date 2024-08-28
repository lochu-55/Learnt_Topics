*** Settings ***
Library  SeleniumLibrary
Resource    ../Resources/resources.robot


*** Variables ***
${browser}  headlesschrome
${url}  https://demo.guru99.com/test/newtours/

*** Test Cases ***
TC1
    ${pageTitle}=   LoginBrowser    ${url}    ${browser}

    log to console    ${pageTitle}
    log    ${pageTitle}
    input text    userName  lochu5viehya@gmail.com
    input text    password      Lovely@3455
    close browser
