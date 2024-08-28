*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/login_resources.robot
Library  DataDriver  file=TestData/LoginData.xlsx

Suite Setup    Opening
Suite Teardown    Closing
Test Template    Invalid Login

*** Test Cases ***
LogintestWithExcel using ${usr} ${pswd}

*** Keywords ***
Invalid Login
    [Arguments]    ${usr}   ${pswd}
    Input username  ${usr}
    Input Password  ${pswd}
    Login button
    Error Message
