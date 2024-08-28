*** Settings ***


*** Test Cases ***
RegTest
    [Tags]    regression
    log to console    this is registration test
    log to console    registration is over

logintest
    [Tags]    sanity
    log to console    this is login test
    log to console    login test is over

ChangeUser
    [Tags]    regression
    log to console    this is changing username test
    log to console    changing is done

LogOut
    [Tags]    sanity
    log to console    this is logging out test
    log to console    logging is out is done