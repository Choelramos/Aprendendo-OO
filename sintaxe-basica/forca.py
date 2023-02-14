import random

def jogar():

    apresentacao_jogo()
    palavra_secreta = abre_arquivo_palavras()
    lista = inicializa_letras_acertadas(palavra_secreta)
    print(lista)

    acertou = False
    enforcou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = chute_escolhido()

        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, lista)

        else:
            erros += 1
            print("Você errou, ainda tem {} tentativas".format(7 - erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in lista

        print(lista)

    if(acertou):
        jogador_venceu()

    else:
        jogador_perdeu(palavra_secreta)


def apresentacao_jogo():
    print("*************************************")
    print("Bem vindo ao meu jogo de Forca!")
    print("*************************************")


def abre_arquivo_palavras():

    arquivo = open("palavras.txt", "r")

    palavras = []
    for linha in arquivo:  # para cada linha no arquivo>
        linha = linha.strip()  # usamos o strip para tirar os '\n' do arquivo
        palavras.append(linha)  # usado para adicionar palavras a nossa lista de palavras

    arquivo.close()

    numero = random.randrange(0, len(palavras))  # para cada linha na lista de palavras, adicionamos um numero aleatório
    palavra_secreta = palavras[numero].upper()  # estamos usando o numero aleatório como índice para a lista de palavras
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]  # escrito dessa forma chamamos de List Comprehension


def chute_escolhido():
    chute = input("Escolha uma letra: ")
    chute = chute.strip().upper()  # this function serves to remove spaces
    return chute


def marca_chute_correto(palavra_secreta, chute, lista):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            lista[index] = letra
        index += 1


def jogador_venceu():
    imprime_mensagem_vencedor()


def jogador_perdeu(palavra):
    imprime_mensagem_perdedor(palavra)


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {} !".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()
