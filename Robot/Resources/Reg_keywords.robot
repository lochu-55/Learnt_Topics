*** Settings ***
Library     SeleniumLibrary
Variables    ../PageObjects/Locator.py

*** Keywords ***
Open_my_browser
    [Arguments]    ${url}   ${browser}
    open browser    ${url}  ${browser}
    maximize browser window

click reg link
    click link  ${link_Reg}

Enter firstname
    [Arguments]    ${firstname}
    input text     ${txt_firstname}   ${firstname}

Enter lastname
    [Arguments]    ${lname}
    input text  ${txt_lastname}     ${lname}

Enter phone
    [Arguments]    ${phone}
    input text  ${txt_phone}    ${phone}

Enter email
    [Arguments]    ${email}
    input text  ${txt_email}    ${email}

Enter address1
    [Arguments]    ${add1}
    input text  ${txt_add1}     ${add1}

Enter city
    [Arguments]    ${city}
    input text  ${txt_city}     ${city}

Enter state
    [Arguments]    ${state}
    input text  ${txt_state}        ${state}

Enter postal code
    [Arguments]    ${postalcode}
    input text      ${txt_postCode}    ${postalcode}

Select country
    [Arguments]    ${country}
    select from list by label   ${txt_country}  ${country}

Enter username
    [Arguments]    ${username}
    input text  ${txt_username}     ${username}

Enter password
    [Arguments]    ${pswd}
    input text      ${txt_password}    ${pswd}

Enter confirm password
    [Arguments]    ${confrmpwd}
    input text     ${txt_confrmpwd}     ${confrmpwd}

Click Submit
    click button    ${btn_submit}

Successful register
    title should be     Register: Mercury Tours

Enter loginusername
    [Arguments]    ${user}
    Input text  ${txt_loginusername}    ${user}

Enter loginpassword
    [Arguments]    ${pswd}
    Input text     ${txt_loginpassword}    ${pswd}

Click SignIn
    click button    //input[@name='submit']

Successful login
    title should be     Login: Mercury Tours

Closing
    close all browsers