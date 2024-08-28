*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Reg_keywords.robot


*** Variables ***
${browser}  headlesschrome
${siteURL}  https://demo.guru99.com/test/newtours/




*** Test Cases ***
Registration Test
    set selenium speed  0.5
    Open_my_browser     ${siteURL}   ${browser}
    click reg link
    Enter firstname     Lochani Vilehya
    Enter lastname      Surisetti
    Enter phone     8328670983
    Enter email     lochu5vilehya@gmail.com
    Enter address1      India
    Enter city      Rajahmundry
    Enter state     Andhra Pradesh
    Enter postal code   533102
    Select country      CANADA

    Enter username  lochu-55
    Enter password  Lovely@3455
    Enter confirm password  Lovely@3455
    Click Submit
    Successful register
    go to   https://demo.guru99.com/test/newtours/index.php
    Enter loginusername     lochu-55
    Enter loginpassword     Lovely@3455
    click SignIn
    Successful login
    Closing