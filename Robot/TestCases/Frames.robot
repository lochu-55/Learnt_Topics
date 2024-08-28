*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://www.w3schools.com/js/tryit.asp?filename=tryjs_array




*** Test Cases ***
Switch to Frame Test
    Open Browser    ${url}   Chrome
    maximize browser window
    set selenium speed    0.5
    select frame    iframeResult
    current frame should contain    JavaScript Arrays
    current frame should not contain    hello
    unselect frame

    frame should contain    iframeResult     JavaScript Arrays
    Close Browser




*** Keywords ***
