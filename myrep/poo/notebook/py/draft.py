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

    def ligar(self):
        if self.__ligado:
            return
        if self.__carregador or (self.__bateria and self.__bateria.getCarga() > 0):
            self.__ligado = True
            print("Notebook esta ligado")
        else:
            print("fail: notebook nao pode ser ligado")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("Notebook esta desligado")

    def rmBateria(self):
        if self.__bateria:
            temp = self.__bateria
            self.__bateria = None
            print("bateria removida")
            return temp
        return None
        
    def rmCarregador(self):
        if self.__carregador:
            temp = self.__carregador 
            self.__carregador = None
            print("carregador removido")
            return temp
        return None

    def usar(self, tempo: int):
        if not self.__ligado:
            return
        if self.__bateria != None and self.__carregador != None:
            print("fail: sem bateria e sem carregador")
            return      
        if self.__carregador:

            carga = self.__bateria.setCarga()
            if carga <= 0:
                print("carga vazia")
                self.__ligado = False 
                return
            new_carga = carga - tempo
            if new_carga <= 0:
                self.__bateria.getCarga(0)
                self.__ligado = False
            else:
                self.__bateria.setCarga(new_carga)
    
    def __str__(self) -> str:
        estado = "ligado" if self.__ligado else "desligado\n"
        saida = f"Notebook: {estado}"
        if self.__bateria != None:
            saida += f"Bateria: {self.__bateria}\n"
        else:
            saida += f"Bateria nao conectada"
        if self.__carregador != None:
            saida += f"Carregador: {self.__carregador}\n"
        else:
            saida += f"Carregador nao conectado"
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
        self.__potencia: int = 1

    def getPotencia(self):
        return self.__potencia
    
    def setPotencia(self, potencia: int):
        if potencia > 0:
            self.__potencia = potencia

    def __str__(self) -> str:
        return f"potencia {self.__potencia}"
    
def main():
        notebook = Notebook()
        bateria = Bateria(50)
        carregador = Carregador(3)
        
        while True:
            line: str = input()
            print("$" + line)
            args: list[str]  = line.split(" ")
            if args[0] == "end":
                break
            elif args[0] == "show":
                print(notebook)
            elif args[0] == "ligar":
                notebook.ligar()
            elif args[0] == "desligar":
                notebook.desligar()
            elif args[0] == "rmBateria":
                notebook.rmBateria()
            elif args[0] == "rmCarregador":
                notebook.rmCarregador()
            elif args[0] == "setCarregador":
                potencia = int(args[1])
                carregador = Carregador(potencia)
                notebook.setCarregador(carregador)




main()