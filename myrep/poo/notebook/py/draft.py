class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None

    def getLigado(self) -> bool:
        return self.__ligado
    
    def setBateria(self, bateria):
        self.__bateria = bateria
    
    def __ste__(self) -> str:
        saida = ""
        saida += f"Notebook:{"ligado" if self.__ligado else "desligado"}"
        if self.__bateria != None:
            saida + f"Bateria: {self.__bateria}"
    
class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade
 
    def getCapacidade(self) -> int:
        return self.__capacidade
    
    def getCaega(self) -> int:
        return self.__carga

    def __str__(self) -> str:
        return f"bateria: {self.__capacidade}:{self.__carga}"