*** Settings ***
Library     Browser
Resource    ../environment_config.robot


*** Variables ***
${EXEMPLE}      xpath=//


*** Keywords ***
Example Keyword
    [Documentation]    This is an example keyword.
    New Browser
