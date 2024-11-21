def resumo():
    mensagem = (
        "Grace Hopper foi uma cientista da computação e oficial da Marinha dos EUA, "
        "pioneira na programação de computadores e criadora do primeiro compilador, "
        "além de contribuir para o desenvolvimento da linguagem COBOL."
    )
    return mensagem


def doutorado():
    mensagem = (
        "Grace Hopper obteve seu doutorado em Matemática pela Universidade de Yale em 1934, "
        "sendo uma das poucas mulheres de sua época a alcançar esse feito."
    )
    return mensagem


def contribuicoes():
    mensagem = (
        "Hopper foi fundamental na criação do primeiro compilador de computadores, "
        "que converte linguagem humana em código de máquina, e liderou o desenvolvimento "
        "do COBOL, uma linguagem de programação amplamente utilizada até hoje."
    )
    return mensagem


def artigos():
    mensagem = (
        "Embora Grace Hopper não seja amplamente reconhecida por artigos acadêmicos, "
        "suas palestras e documentos técnicos sobre compiladores e o COBOL são marcos históricos. "
        "Ela também popularizou o termo 'debugging' no contexto de computação."
    )
    return mensagem


def citacoes():
    mensagem = (
        "Uma das citações mais famosas de Grace Hopper é: "
        "'A phrase I hear often is, 'But we've always done it this way.' "
        "Essa atitude é mortal para qualquer organização.'"
    )
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Grace Hopper.\n")

continuar = True
while continuar:

    opcao = int(
        input(
            """
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
