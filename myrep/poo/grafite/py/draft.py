class Grafite:
    def __init__(self, calibre:float, hardness:str, size:int ):
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
        if self.__calibre == 'HB':
            return 1
        elif self.__calibre == '2B':
            return 2
        elif self.__calibre == "4B":
            return 4
        elif self.__calibre == "6B":
            return 6
        return 0
    
    def __str__(self):
        return f"{self.__calibre}:{self.__hardness}: {self.__size}"
    
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
            print("fail: calibre incompativel")
            return False
        if grafite.getCalibre() != self.__calibre:
            print("fail: ja existe grafite")
            return False
        self.__ponta = grafite
        return True
   
    def remove(self) -> Grafite | None:
        if self.HasGrafite():
            self.__ponta = None
        else:
            print("fail: nao existe grafite")

    def writePage(self) -> None:
        if self.HasGrafite():
            grafite = self.__ponta

    def __str__(self) -> str:
        return f"calibre:{self.__calibre}: grafite:{self.__ponta}"
    

def main():
    pencil = Pencil(0)
    while True:
        line: str = input("")
        print("$" + line)
        args: list[str] = line.split(" ")
        




main()
