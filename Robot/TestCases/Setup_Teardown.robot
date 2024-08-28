*** Settings ***

Suite Setup    log to console   Opening
Suite Teardown    log to console  Closing

Test Setup    log to console    login into app
Test Teardown    log to console     logout to app



*** Test Cases ***
Prepaid recharge
    log to console    this is prepaid recharge

Postpaid recharge
    log to console    this is postpaid recharge

Search
    log to console    this is search test case

Advanced search
    log to console    this is advanced search test case