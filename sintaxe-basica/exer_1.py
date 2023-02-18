# Um pequeno exercício onde deve implementar um programa, criando
# a classe veículo com atributos de instância "velocidade máxima" e
# quilômetros percorricos por litro"

class Veiculo:
    def __init__(self, nome, vl_maxima, km_litro):
        self.nome = nome
        self.vl_maxima = vl_maxima
        self.km_litro = km_litro

    def qnt_acentos(self, capacidade):
        print(f'A capacidade de acentos do veículo {self.nome} é: {capacidade}')

    def mostra_dados(self):
        print(f'Nome = {self.nome}')
        print(f'Velocidade máxima= {self.vl_maxima}')
        print(f'Quilometros por litro = {self.km_litro} \n')


modelo_carro = Veiculo("Corsa", 180, 15)
modelo_carro.mostra_dados()

# Criando uma classe filha que herrada os atributos da classe Veiculo


class Onibus(Veiculo):
    def qnt_acentos(self, capacidade=70):
        return super().qnt_acentos(capacidade=70)


busao = Onibus("Mercedes 12T", 120, 5)
busao.qnt_acentos()
