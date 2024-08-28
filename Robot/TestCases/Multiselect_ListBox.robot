*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://techcanvass.com/Examples/multi-select.html


*** Test Cases ***
Testing ListBox
    open browser    ${url}    ${browser}
    maximize browser window
    set selenium speed    0.5
    LoginToApp
    close browser



*** Keywords ***
LoginToApp
    select from list by label   multiselect  Audi
    select from list by index   multiselect  1
    select from list by value   multiselect  honda
    sleep    3
    unselect from list by label    multiselect  Audi
    unselect from list by index    multiselect  4
    click element   xpath://input[@type='submit']
    sleep   2

