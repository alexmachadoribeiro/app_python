from deep_translator import GoogleTranslator

try:
    # instanciando objeto tradutor
    tradutor = GoogleTranslator(source="auto", target="pt")

    # laço de repetição
    while True:
        # declaração de variáveis
        texto_original = input("Digite o texto a ser traduzido em qualquer idioma: ")
        texto_traduzido = tradutor.translate(texto_original)

        # exibe o texto traduzido
        print(f'Texto traduzido: "{texto_traduzido}"\n')

        # informa se deseja traduzir outro texto ou encerrar
        encerrar = input("Deseja traduzir outro texto? (s/n)")

        match encerrar:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")
except Exception as e:
    print(f"Não foi possível traduzir. {e}.")