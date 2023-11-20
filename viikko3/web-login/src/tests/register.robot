# Vinkki: voit halutessasi toteuttaa login_resource.robot-tiedoston
*** Settings ***
Resource  resource.robot
Library  ../AppLibrary.py
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Setup Register

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirm  kalle456
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle456
    Set Password Confirm  kalle456
    Submit Credentials
    Register Should Fail With Message  Username length should be at least 3.


Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekalle
    Set Password Confirm  kallekalle
    Submit Credentials
    Register Should Fail With Message  Password should contain characters different from a-z

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirm  kalle457
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirm  kalle456
    Submit Credentials
    Register Should Succeed
    Go To Main Page
    Click Button  Logout
    Go To Login Page
    Set Username  kalle
    Set Password  kalle456
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirm  kalle457
    Submit Credentials
    Register Should Fail With Message  Passwords do not match
    
    Go To Login Page
    Set Username  kalle
    Set Password  kalle456
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Setup Register
    Reset Application
    Go To Register Page
    Register Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirm
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
