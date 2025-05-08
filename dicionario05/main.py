chaves = ("nome", "idade", "cpf", "telefone", "email", "profissão")
usuario = {
    chaves[0]: "Alex Machado",
    chaves[1]: 40,
    chaves[2]: "666.666.666-66",
    chaves[3]: "(61) 96666-6666",
    chaves[4]: "alex@gmail.com",
    chaves[5]: "Programador"
}

for chave in usuario:
    print(f"{chave.title()}: {usuario.get(chave)}")