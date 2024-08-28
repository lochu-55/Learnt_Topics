*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area

*** Test Cases ***
Mouse Actions
    set selenium speed    0.5
    open browser    ${url}    ${browser}
    maximize browser window
    execute javascript    window.scrollTo(0,document.body.scrollHeight)     #end of the page
    sleep   2
    execute javascript    window.scrollTo(0,-document.body.scrollHeight)    #top of the page
    sleep   2
    close browser
