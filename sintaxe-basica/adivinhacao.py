import random
def jogar():
    print("*************************************")
    print("Bem vindo ao meu jogo de adivinhação!")
    print("*************************************")

    pontos = 1000
    numero_secreto = round(random.randrange(1, 101))
    total_tentativas = 0

    print("Níveis: 1(Fácil), 2(Médio), 3(Difícil): ", numero_secreto)
    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas = 5
    else:
        total_tentativas = 3

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Digite seu numero: ")
        chute = int(chute_str)

        if(chute < 0 or chute > 100):
            print("Você deve chutar um número entre 0 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break
        else:
            if(maior):
                print("Seu número é maior que o número secreto!")
            elif(menor):
                print("Seu chute foi menor que o numero secreto!")

        pontos_perdidos = abs(chute - numero_secreto)
        total_pontos = pontos - pontos_perdidos

    print("Fim de jogo, seu total de pontos foi: {}".format(total_pontos))

if(__name__== "__main__"): #chama o jogo, caso seja chamada a função principal
    jogar()
