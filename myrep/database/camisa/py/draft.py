class Camisa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str):
        tamanhosValidos = ["PP", "P", "M", "G", "GG", "XG"]

        if valor not in tamanhosValidos:
            print("fail tamanho invalido")
            return
        
        self.__tamanho = valor

camisa = Camisa()
while camisa.getTamanho() == "":
    print("Digite o seu tamanho de roupa")
    tamanho = input()
    camisa.setTamanho(tamanho)
print(f"Parabens, você comprou uma roupa tamanho", camisa.getTamanho())

