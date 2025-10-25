class Grafite:
    def __init__ (self, calibre:float, hardness:str, size:int ):
        self.__calibre = calibre
        self.__hardness = hardness
        self.__size = size

    def getcalibre(self):
        return self.__calibre
    
    def getHardness(self):
        return self.__hardness
    
    def getSize(self):
        return self.__size
    
    def setSize(self, size:int):
        self.__size = size
    
    def usagepersheet(self) -> int:
        if self.__hardness == 'HB':
            return 1
        elif self.__hardness == '2B':
            return 2
        elif self.__hardness == "4B":
            return 4
        elif self.__hardness == "6B":
            return 6
        return 0
    
    def __str__(self):
        return f"{self.__calibre}:{self.__hardness}:{self.__size}"
    
class Pencil:
    def __init__(self, calibre: float):
        self.__calibre = calibre
        self.__ponta: Grafite | None = None

    def HasGrafite(self) -> bool:
        if self.__ponta != None:
            return True
        else:
            return False

    def insert(self, grafite: Grafite) -> bool:
        if self.HasGrafite():
            print("fail: ja existe grafite")
            return False
        if grafite.getcalibre() != self.__calibre:
            print("fail: calibre incompativel")
            return False
        self.__ponta = grafite
        return True
   
    def remove(self) -> Grafite | None:
        if self.HasGrafite():
           g = self.__ponta
           self.__ponta = None
           return g
        else:
            print("fail: nao existe grafite")
            return None

    def writePage(self) -> None:
        if self.HasGrafite() == False:
            print("fail: nao existe grafite")
            return
        
        gasto = self.__ponta.usagepersheet()
        tam_A = self.__ponta.getSize()
        if self.__ponta.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return

        if tam_A - gasto < 10:
            self.__ponta.setSize(10)
            print("fail: folha incompleta")
            return
        
        self.__ponta.setSize(tam_A - gasto)

    def __str__(self) -> str:
        aux = ""
        if self.__ponta != None:
            aux = f"[{self.__ponta}]"
        else:
            aux = "null"
        return f"calibre: {self.__calibre}, grafite: {aux}"
    

def main():
    pencil: Pencil | None = None
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pencil)
        elif args[0] == "init":
            calibre = float(args[1])
            pencil = Pencil(calibre)
        elif args[0] == "remove":
            if pencil:
                pencil.remove()
            else:
                print("fail: remover")
        elif args[0] == "insert":
            if not pencil:
               print("fail")
               continue
            teste = Grafite(float(args[1]),(args[2]), int (args[3]))
            pencil.insert(teste)
        elif args[0] == "write":
                pencil.writePage()




main()
