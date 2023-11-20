*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists
    
Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least 3 characters long.

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  kall€  kalle123
    Output Should Contain  Username should only consist of characters a-z.

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kalle  kalle12
    Output Should Contain  Password must be at least 8 characters long.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password should not only consist of characters a-z.
