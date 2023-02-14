import forca
import adivinhacao

def escolhe_jogo():
    print("***************************")
    print("Bem vindo a lista de jogos!")
    print("***************************")

    print("Opção 1 *Adivinhação* ou opção 2 *Forca*")
    jogos = int(input("Qual jogo?"))

    if(jogos == 1):
        print("Carregando jogo da Adivinhação!")
        adivinhacao.jogar()
    else:
        print("Carregando jogo da Forca!")
        forca.jogar()

if(__name__=="__main__"):
    escolhe_jogo()
