class Chinela:
    def __init__(self):
     self.__tamanho = 0

    def getTamanho(self):
       return self.__tamanho
    
    def setTamanho(self, valor: int):
       if valor < 20 or valor > 50 or valor % 2 != 0:
            print("")
            return
        
            self.__tamanho = valor

chinela = Chinela()

while chinela.getTamanho() == 0:
    print("digite o valor do seu chinela")
    tamanho = int(input())
    chinela.setTamanho(tamanho)
print(f"O seu chinelo tem tamanho {chinela.getTamanho()}")