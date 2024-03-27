*** Settings ***
Library       Selenium2Library    timeout=10   implicit_wait=1.5   run_on_failure=Capture Page Screenshot

*** Variables ***
${browser}  Chrome
${url}  https://ecalc.ru/tdee/?ysclid=lu3tmwq4ek206410734
*** Keywords ***
Calculate
    [Arguments]    ${sex}     ${nage}     ${nheight}    ${nweight}    ${activity}     ${result}
    Open Browser    ${url}    ${browser}

#-------------Вычисление фактического реузльтата (мужчины)------------------#
    Select From List By Index  id=sex    ${sex}
    Input Text    id=nage    ${nage}
    Input Text    id=nheight    ${nheight}
    Input Text    id=nweight    ${nweight}
    Select From List By Index       id=activity    ${activity}
    Sleep    5
    ${result_field}    Get Text    id=resulttdee
    Should Be Equal    ${result}    ${result_field}
    Close Browser


*** Test Cases ***

Положительные числа:
    Calculate    1    30    180    120    1    2417





