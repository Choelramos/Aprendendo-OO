class Argentina:
    def capital(self):
        print("A capital da Argentina é Buenos Aires")

    def lingua_falada(self):
        print("A língua falada na Argentina é Espanhol")


class Brasil:
    def capital(self):
        print("A capital do Brasil é Brasília")

    def lingua_falada(self):
        print("A língua falada no Brasil é Português")


obj_argentina = Argentina()
obj_brasil = Brasil()


for pais in (obj_argentina, obj_brasil):
    pais.capital()
    pais.lingua_falada()
    print(pais)