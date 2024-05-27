def mad_libs():
    print("Bem-vindo ao Jogo Mad Libs!")
    print("Por favor, forneça algumas palavras para preencher as lacunas:")

    # Solicitar palavras ao usuário
    nome = input("Digite um nome: ")
    adjetivo = input("Digite um adjetivo: ")
    verbo = input("Digite um verbo no infinitivo: ")
    objeto = input("Digite um objeto: ")

    # Mostrar a história com as palavras do usuário
    print("\nAqui está a sua história:")
    print(f"\nUma vez, {nome} estava andando na floresta quando encontrou um {adjetivo} {objeto}.")
    print(f"{nome} ficou tão surpreso que decidiu {verbo} imediatamente!")

# Chamar a função para jogar Mad Libs
mad_libs()