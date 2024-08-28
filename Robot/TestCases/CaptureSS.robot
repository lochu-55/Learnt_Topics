*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login


*** Test Cases ***
Capture Screenshot
    set selenium speed    0.5
    open browser    ${url}    ${browser}
    maximize browser window
    input text    username  Admin
    input text    password      admin123
    #capture element screenshot    //*[@id="app"]/div[1]/div/div[1]/div/div[1]/img       C:/Users/vlab/PycharmProjects/Robot/logo.png
    #capture page screenshot      C:/Users/vlab/PycharmProjects/Robot/OrangePage.png
    capture element screenshot    //*[@id="app"]/div[1]/div/div[1]/div/div[1]/img   logo1.png
    capture page screenshot    login.png
    close browser