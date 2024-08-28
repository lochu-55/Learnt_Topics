*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Register.html

*** Test Cases ***
LoginTest
    open browser    ${url}    ${browser}
    LoginToApp
    close browser



*** Keywords ***
LoginToApp
    click link    xpath://a[@href="Index.html"]
    sleep    2s
    input text    id:email  lochu5vilehya@gmail.com
    sleep    2s
    click element    id:enterimg
    sleep    2s