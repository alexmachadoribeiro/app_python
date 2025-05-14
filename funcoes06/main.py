# importa biblioteca
import time
import modulo as m

# algoritmo principal
if __name__ == "__main__":
    nome = input("Informe o nome do aluno: ")
    resultado = m.verificar_matricula(nome)
    for verificacao in resultado:
        time.sleep(3)
        print(verificacao)