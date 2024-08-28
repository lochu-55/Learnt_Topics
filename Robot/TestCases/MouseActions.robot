*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://swisnl.github.io/jQuery-contextMenu/3.x/demo.html
${url1}     https://testautomationpractice.blogspot.com/
${url2}     http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette
*** Test Cases ***
Mouse Actions
    set selenium speed    0.5
    open browser    ${url}    ${browser}
    maximize browser window
    open context menu    xpath:/html/body/div/section/div/div/div/p/span


    go to    ${url1}
    double click element    //*[@id="HTML10"]/div[1]/button

    go to   ${url2}
    drag and drop    id:box6    id:box106
    sleep    2

    close browser