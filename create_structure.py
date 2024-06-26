import os


def create_project_structure(project_name):
    # Definindo a estrutura
    directories = [
        f"{project_name}/tests",
        f"{project_name}/Resources",
        f"{project_name}/results",
    ]

    files = {
        f"{project_name}/resources/common_ui_resource.robot": "*** Settings ***\nLibrary          Browser\nResource          ../environment_config.robot\n\n*** Variables ***\n${EXEMPLE}          xpath=//\n\n*** Keywords ***\nExample Keyword\n    [Documentation]    This is an example keyword.\n     New Browser",
        f"{project_name}/tests/example_test.robot": "*** Settings ***\nResource  ../Resources/common_ui_resource.robot\n\n*** Test Cases ***\nExample Test\n     [Documentation]\n     Given Exemple1\n     When Exemplo2\n     Then Exemplo3",
        f"{project_name}/.gitignore": "*.pyc\n__pycache__/\nresults/\n",
        f"{project_name}/environment_config.robot": "*** Variables ***\n#INFO LAB\n${BROWSER}          chromium\n${LAB}          10\n${ADDRESS_LAB}          10.10.10.${LAB}\n${URL}          https://${ADDRESS_LAB}\n\n#UI CREDENTIALS\n${USERNAME_LAB}       robot.admin\n${PASSWORD_LAB}       123123123",
    }

    # Criando diretórios
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Criando arquivos
    for file_path, file_content in files.items():
        with open(file_path, "w") as file:
            file.write(file_content)

    print(f"Estrutura de projeto '{project_name}' criada com sucesso!")


# # Use o nome do seu projeto
create_project_structure("meu_projeto_robot")
