*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.automationtesting.in/Register.html


*** Test Cases ***
LoginTest
    open browser    ${url}    ${browser}
    maximize browser window
    title should be     Register
    LoginToApp
    close browser



*** Keywords ***
LoginToApp
    click link    xpath://a[@href="Index.html"]
    sleep    2s
    title should be     Index

    ${"email_txt"}  set variable    id:email

    element should be visible   ${"email_txt"}
    element should be enabled   ${"email_txt"}

    input text    ${"email_txt"}  lochu5vilehya@gmail.com
    sleep    2

    clear element text    ${"email_txt"}
    sleep    3

