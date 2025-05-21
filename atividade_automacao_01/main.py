import pyautogui as p

def limpar_credenciais():
    p.write("git config --global --unset user.name")
    p.press("enter")
    p.write("git config --global --unset user.email")
    p.press("enter")

if __name__ == "__main__":
    p.PAUSE = 0.5

    msg_commit = input("Informe a mensagem do commit: ")

    # p.hotkey("ctrl", "j")

    limpar_credenciais()

    p.write('git config --global user.name "alexmachadoribeiro"')
    p.press("enter")
    p.write('git config --global user.email "alex.ribeiro@df.docente.senai.br"')
    p.press("enter")
    p.write("git add .")
    p.press("enter")
    p.write(f'git commit -m "{msg_commit}"')
    p.press("enter")
    p.write("git push")
    p.press("enter")

    limpar_credenciais()

# TODO - atividade
"""
Crie um programa que commita o projeto de vocês e envia o repositório para o GitHub.
"""