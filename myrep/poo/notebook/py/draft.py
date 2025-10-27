class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def getLigado(self) -> bool:
        return self.__ligado
    
    def setBateria(self, bateria):
        self.__bateria = bateria

    def setCarregador(self, carregador):
        self.__carregador = carregador

    def usar(self, tempo: int):
        if self.__bateria != None and self.__carregador != None:
            potencia = self.__carregador.getPotencia()
            mais = potencia * tempo
            self.__bateria.setCarga(self.__bateria.getCarga() + mais)
    
    def __str__(self) -> str:
        estado = "ligado" if self.__ligado else "desligado\n"
        saida = f"Notebook: {estado}"
        if self.__bateria != None:
            saida += f"Bateria: {self.__bateria}\n"
        else:
            saida += f"Bateria: nao conectada"

        return saida
    
class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade
        self.__carga: int = 0
 
    def getCapacidade(self) -> int:
        return self.__capacidade
    
    def getCarga(self) -> int:
        return self.__carga
    
    def setCarga(self, carga):
        self.__carga = carga

    def __str__(self) -> str:
        return f"bateria: {self.__carga}:{self.__capacidade}"
    
class Carregador:
    def __init__(self, potencia):
        self.__potencia: int = potencia

    def getPotencia(self):
        return self.__potencia
    
    def setPotencia(self, potencia: int):
        if potencia > 0:
            self.__potencia = potencia

    
def main():
        notebook = Notebook()
        bateria = Bateria(50)
        notebook.setBateria(bateria)
        carregador = Carregador(3)
        notebook.setCarregador(carregador)

        while True:
            line: str = input()
            print("$" + line)
            args: list[str]  = line.split(" ")
            if args[0] == "end":
                break
            elif args[0] == "show":
                print(notebook)

main()