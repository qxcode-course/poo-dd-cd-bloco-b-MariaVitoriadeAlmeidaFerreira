class Camisa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str):
        tamanhosValidos = ["PP", "P", "M", "G", "GG", "XG"]