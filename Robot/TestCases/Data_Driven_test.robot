*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/login_resources.robot
Suite Setup    Opening
Suite Teardown    Closing
Test Template    Invalid Login

*** Test Cases ***          usr                     pswd
Right user empty pass       admin@yourstore.com     ${EMPTY}
Right user wrong pass       admin@yourstore.com     hello
wrong user right pass       admn@yourstore.com      admin
wrong usr wrong pass        admin@yourstore.co      ad
wrong user empty pass       admin@yourstore.co      ${EMPTY}




*** Keywords ***
Invalid Login
    [Arguments]    ${usr}   ${pswd}
    Input username  ${usr}
    Input Password  ${pswd}
    Login button
    Error Message


